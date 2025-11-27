<img width="1384" height="899" alt="image" src="https://github.com/user-attachments/assets/0d093631-e0b0-4d80-9398-309fc3f9e5d2" />

# FandomK AI Recommendation API

K-POP 아이돌 추천 시스템 - Sentence Transformers 기반 의미 유사도 추천

https://fandom-k-blue.vercel.app/

## 📌 프로젝트 소개

사용자가 선택한 아이돌과 유사한 다른 아이돌을 추천해주는 AI 시스템입니다.

- **Sentence Transformers**를 사용한 텍스트 임베딩
- **코사인 유사도** 기반 추천
- **FastAPI**로 구현한 RESTful API

## 🛠️ 기술 스택

- **Python 3.13**
- **FastAPI** - 웹 API 프레임워크
- **Sentence Transformers** - 한국어 지원 임베딩 모델
- **scikit-learn** - 코사인 유사도 계산
- **NumPy** - 벡터 연산

## 📦 설치 방법

### 1. 가상환경 생성 및 활성화

```bash
# Windows
python -m venv venv
.\venv\Scripts\Activate.ps1

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. 패키지 설치

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### 3. 서버 실행
- 현재는 허깅페이스에 도커화하여 배포 완료되어서 아래처럼 실행하지 않아도 추천 기능이 작동합니다.

```bash
python -m uvicorn main:app --reload
```

서버가 실행되면 다음 주소로 접속:

- **API 서버**: http://127.0.0.1:8000
- **API 문서 (Swagger)**: http://127.0.0.1:8000/docs

## 🚀 API 사용법

### POST `/api/recommend`

선택한 아이돌과 유사한 아이돌 추천

**요청 예시:**

```json
{
  "selected_idol_ids": [7995, 7987],
  "limit": 8
}
```

**응답 예시:**

```json
{
  "recommended_ids": [7975, 7988, 7989, 7979],
  "scores": [0.931, 0.916, 0.915, 0.902]
}
```

## 🧠 추천 시스템 작동 원리

1. **텍스트 임베딩 생성**

   - 아이돌 정보 (이름, 성별, 그룹, 장르, 소속사)를 자연어 문장으로 변환
   - Sentence Transformer 모델로 벡터화

2. **유사도 계산**

   - 선택한 아이돌들의 임베딩 평균 계산
   - 모든 아이돌과의 코사인 유사도 측정

3. **추천 결과 반환**
   - 유사도가 높은 순서대로 정렬
   - 이미 선택된 아이돌 제외

## 📂 프로젝트 구조

```
recommendation-api/
├── main.py                 # FastAPI 앱 진입점
├── requirements.txt        # Python 패키지 목록
├── models/
│   ├── __init__.py
│   ├── recommender.py      # 추천 엔진 핵심 로직
│   └── idol_metadata.py    # 그룹별 메타데이터
└── README.md
```

## 📝 주요 파일 설명

### `main.py`

- FastAPI 애플리케이션 정의
- CORS 설정
- API 엔드포인트 구현

### `models/recommender.py`

- Sentence Transformer 모델 로드
- 아이돌 데이터 API 호출
- 임베딩 생성 및 유사도 계산

### `models/idol_metadata.py`

- 그룹별 소속사, 장르 정보
- 자연어 설명 템플릿

## 🔧 커스터마이징

### 그룹 메타데이터 추가

`models/idol_metadata.py`에서 그룹 정보를 추가할 수 있습니다:

```python
GROUP_METADATA = {
    "그룹명": {
        "agency": "소속사",
        "genres": ["장르1", "장르2"],
        "description": "자연어 설명"
    }
}
```

## 📌 참고사항

- **첫 실행 시**: Sentence Transformer 모델 다운로드 (~500MB, 1-2분 소요)
- **재실행 시**: 로컬 캐시에서 로드 (빠름)
- **추천 정확도**: 그룹 메타데이터가 있는 경우 더 정확

