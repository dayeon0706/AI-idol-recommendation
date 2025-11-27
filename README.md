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

https://fandom-k-blue.vercel.app/

## 📌 프로젝트 소개

- 선택한 아이돌 기반 유사 아이돌 추천
- 멀티링구얼 문장 임베딩 (한국어, 영어 지원)
- 코사인 유사도 기반 추천 알고리즘

## 🚀 API 사용법

### POST `/api/recommend`

선택한 아이돌과 유사한 아이돌 추천

**요청 예시:**

```json
{
  "selected_idol_ids": [7979, 7995],
  "limit": 8
}
```

**응답 예시:**

```json
{
  "recommended_ids": [7986, 8001, ...],
  "scores": [0.95, 0.92, ...]
}
```

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

> 현재는 Hugging Face Space에 Docker로 배포되어 있어서 로컬 실행 없이도 추천 기능이 작동합니다.

로컬에서 테스트하려면:

```bash
python -m uvicorn main:app --reload
```

서버가 실행되면 다음 주소로 접속:

- **API 서버**: http://127.0.0.1:8000
- **API 문서 (Swagger)**: http://127.0.0.1:8000/docs

## 🐳 Docker 실행

```bash
docker build -t fandomk-ai .
docker run -p 7860:7860 fandomk-ai
```

## 🛠 기술 스택

- **FastAPI**: Python 웹 프레임워크
- **Sentence Transformers**: 문장 임베딩 모델
- **scikit-learn**: 코사인 유사도 계산
- **PyTorch**: 딥러닝 백엔드

## ⚠️ 참고사항

- **첫 실행 시**: Sentence Transformer 모델 다운로드 (~500MB, 1-2분 소요)
- **재실행 시**: 로컬 캐시에서 로드 (빠름)
- **추천 정확도**: 그룹 메타데이터가 있는 경우 더 정확
