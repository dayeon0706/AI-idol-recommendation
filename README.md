---
title: FandomK AI Recommendation
emoji: 🎤
colorFrom: pink
colorTo: purple
sdk: docker
pinned: false
---

# FandomK AI Recommendation API

K-POP 아이돌 추천 AI API입니다. Sentence Transformers를 사용하여 사용자가 선택한 아이돌과 유사한 아이돌을 추천합니다.

## 기능

- 선택한 아이돌 기반 유사 아이돌 추천
- 멀티링구얼 문장 임베딩 (한국어, 영어 지원)
- 코사인 유사도 기반 추천 알고리즘

## API 엔드포인트

### POST /api/recommend

선택한 아이돌과 유사한 아이돌을 추천합니다.

**Request Body:**

```json
{
  "selected_idol_ids": [7979, 7995],
  "limit": 8
}
```

**Response:**

```json
{
  "recommended_ids": [7986, 8001, ...],
  "scores": [0.95, 0.92, ...]
}
```

## 로컬 실행

```bash
# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt

# 서버 실행
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Docker 실행

```bash
docker build -t fandomk-ai .
docker run -p 7860:7860 fandomk-ai
```

## 기술 스택

- **FastAPI**: Python 웹 프레임워크
- **Sentence Transformers**: 문장 임베딩 모델
- **scikit-learn**: 코사인 유사도 계산
- **PyTorch**: 딥러닝 백엔드
