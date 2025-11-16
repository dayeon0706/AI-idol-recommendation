from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import httpx
from typing import List, Tuple
import os
from .idol_metadata import get_group_description

class IdolRecommender:
    def __init__(self):
        # 한국어 지원 경량 모델 (캐싱으로 재시작 시 빠름)
        print("Sentence Transformer 모델 로딩 중...")
        self.model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
        print("모델 로딩 완료")
        self.idols_data = []
        self.embeddings = None
        self.idol_id_to_idx = {}
        #self.embeddings_cache = None  # 캐싱용

    async def initialize(self):
        """아이돌 데이터 로드 및 임베딩 생성"""
        # 실제 API에서 아이돌 데이터 가져오기
        await self._fetch_idols_data()

        # 아이돌 프로필을 텍스트로 변환
        idol_texts = self._create_idol_descriptions()

        # 텍스트를 벡터로 변환 (임베딩)
        self.embeddings = self.model.encode(idol_texts, show_progress_bar=True)

        # ID to Index 매핑
        self.idol_id_to_idx = {
            idol['id']: idx
            for idx, idol in enumerate(self.idols_data)
        }

    async def _fetch_idols_data(self):
        """실제 API에서 아이돌 데이터 가져오기"""
        api_url = "https://fandom-k-api.vercel.app/20-2/idols"

        try:
            async with httpx.AsyncClient() as client:
                print(f"API 호출 시작: {api_url}")
                response = await client.get(api_url, params={"pageSize": 100})
                print(f"API 응답 상태: {response.status_code}")
                
                data = response.json()
                print(f"API 응답 데이터 키: {list(data.keys())}")
                print(f"응답 전체 구조: {data}")
                
                self.idols_data = data.get('list', [])
                print(f"아이돌 데이터 로드 완료: {len(self.idols_data)}명")
                
                if self.idols_data:
                    print(f"첫 번째 아이돌 예시: {self.idols_data[0]}")
                else:
                    print(f"ERROR: 'list' 키에 데이터가 없습니다. 전체 응답: {data}")
        except Exception as e:
            print(f"ERROR: API 호출 실패 - {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()
            self.idols_data = []

    def _create_idol_descriptions(self) -> List[str]:
        """아이돌 정보를 자연어 문장으로 변환"""
        descriptions = []
        for idol in self.idols_data:
            # 기본 정보
            gender_kr = "남자" if idol.get('gender') == 'male' else "여자"
            name = idol['name']
            group = idol['group']
            
            # 그룹 메타데이터 가져오기
            group_desc = get_group_description(group)
            
            # 메타데이터가 있으면 풍부한 설명, 없으면 기본 설명
            if group_desc:
                desc = f"{name} {gender_kr} {group} {group_desc}"
            else:
                desc = f"{name} {gender_kr} {group}"
            
            descriptions.append(desc)
        
        print(f"📝 생성된 설명 샘플 (처음 3개):")
        for i, desc in enumerate(descriptions[:3]):
            print(f"  {i+1}. {desc[:100]}...")  # 처음 100자만 출력

        return descriptions

    def get_recommendations(
        self,
        selected_idol_ids: List[int],
        limit: int = 10
    ) -> Tuple[List[int], List[float]]:
        """선택한 아이돌들과 유사한 아이돌 추천"""

        try:
            print(f"추천 요청: 선택된 아이돌 IDs = {selected_idol_ids}")
            print(f"현재 로드된 아이돌 수: {len(self.idols_data)}")

            if not selected_idol_ids:
                print("선택된 아이돌이 없습니다")
                return [], []

            # 데이터 검증
            if not self.idols_data or self.embeddings is None:
                print("ERROR: 아이돌 데이터가 초기화되지 않았습니다")
                return [], []

            # 선택한 아이돌들의 임베딩 평균 계산
            selected_indices = [
                self.idol_id_to_idx[idol_id]
                for idol_id in selected_idol_ids
                if idol_id in self.idol_id_to_idx
            ]

            print(f"매칭된 인덱스: {selected_indices}")
            print(f"전체 ID 매핑 샘플 (처음 5개): {list(self.idol_id_to_idx.items())[:5]}")

            if not selected_indices:
                print(f"ERROR: 선택된 아이돌 ID {selected_idol_ids}가 데이터에 없습니다")
                print(f"사용 가능한 ID 예시: {list(self.idol_id_to_idx.keys())[:10]}")
                return [], []

            # 선택한 아이돌들의 임베딩 평균 (사용자 프로필)
            user_profile = np.mean(self.embeddings[selected_indices], axis=0)
        except Exception as e:
            print(f"ERROR in get_recommendations: {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()
            return [], []

        # 모든 아이돌과의 유사도 계산
        similarities = cosine_similarity(
            [user_profile],
            self.embeddings
        )[0]

        # 이미 선택한 아이돌 제외
        for idx in selected_indices:
            similarities[idx] = -1

        # 유사도 높은 순으로 정렬
        top_indices = np.argsort(similarities)[::-1][:limit]

        # ID와 점수 반환
        recommended_ids = [
            self.idols_data[idx]['id']
            for idx in top_indices
        ]
        scores = [float(similarities[idx]) for idx in top_indices]
        
        # 디버깅: 추천 결과 출력
        print(f"추천 결과 (총 {len(recommended_ids)}개):")
        for idx, (idol_id, score) in enumerate(zip(recommended_ids, scores)):
            try:
                idol = next((x for x in self.idols_data if x['id'] == idol_id), None)
                if idol:
                    gender_kr = "남자" if idol.get('gender') == 'male' else "여자"
                    print(f"  {idx+1}. {idol['name']} {gender_kr} ({idol['group']}) - 유사도: {score:.3f}")
            except Exception as e:
                print(f"  {idx+1}. ID {idol_id} - 에러: {e}")

        return recommended_ids, scores
