---
title: FandomK AI Recommendation
emoji: 🎤
colorFrom: pink
colorTo: purple
sdk: docker
pinned: false
---

<img width="1384" height="899" alt="image" src="https://github.com/user-attachments/assets/0d093631-e0b0-4d80-9398-309fc3f9e5d2" />

# FandomK AI Recommendation API

K-POP 아이돌 추천 AI API입니다. Sentence Transformers를 사용하여 사용자가 선택한 아이돌과 유사한 아이돌을 추천합니다.

🔗 **서비스 URL**: https://fandom-k-blue.vercel.app
🔗 **AI 추천 서비스 사용한 URL**: https://fandom-k-blue.vercel.app/mypage

## 📌 프로젝트 소개

- 선택한 아이돌 기반 유사 아이돌 추천
- 멀티링구얼 문장 임베딩 (한국어, 영어 지원)
- 코사인 유사도 기반 추천 알고리즘

## 🚀 API 사용법

### POST `/api/recommend`

선택한 아이돌과 유사한 아이돌을 추천합니다.

**요청 예시:**

{
  "selected_idol_ids": [7979, 7995],
  "limit": 8
}- `selected_idol_ids`: 사용자가 선택한 아이돌의 ID 배열
- `limit`: 추천받을 아이돌 수 (기본값: 10)

**응답 예시:**

{
  "recommended_ids": [7986, 8001, 7988, 7987, 7985, 7974, 7980, 7982],
  "scores": [0.95, 0.92, 0.89, 0.87, 0.85, 0.83, 0.81, 0.79]
}- `recommended_ids`: 추천된 아이돌의 ID 배열 (유사도 높은 순)
- `scores`: 각 아이돌의 유사도 점수 (0~1 사이 값, 높을수록 유사)

## 🛠 기술 스택

- **FastAPI**: Python 웹 프레임워크
- **Sentence Transformers**: 문장 임베딩 모델 (paraphrase-multilingual-MiniLM-L12-v2)
- **scikit-learn**: 코사인 유사도 계산

## 📡 배포

현재 **Hugging Face Space**에 Docker로 배포되어 있습니다.

- **Space URL**: https://huggingface.co/spaces/Dayeoni/ai-recommendation

## ⚠️ 참고사항

- **첫 실행 시**: Sentence Transformer 모델 다운로드 (~500MB, 1-2분 소요)
