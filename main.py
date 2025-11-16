from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from models.recommender import IdolRecommender

app = FastAPI(title="FandomK AI Recommendation API")

# CORS 설정 (React 앱과 통신)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 개발 중에는 모든 origin 허용
    allow_credentials=False,  # credentials 비활성화 (와일드카드 사용 시 필수)
    allow_methods=["*"],
    allow_headers=["*"],
)

# 전역으로 추천 모델 로드
recommender = IdolRecommender()

class RecommendRequest(BaseModel):
    selected_idol_ids: List[int]
    limit: int = 10

class RecommendResponse(BaseModel):
    recommended_ids: List[int]
    scores: List[float]

@app.on_event("startup")
async def startup_event():
    """서버 시작 시 아이돌 데이터 로드 및 모델 초기화"""
    await recommender.initialize()
    print("AI 추천 모델 초기화 완료")

@app.get("/")
async def root():
    return {"message": "FandomK AI Recommendation API"}

@app.post("/api/recommend", response_model=RecommendResponse)
async def recommend_idols(request: RecommendRequest):
    """선택한 아이돌과 유사한 아이돌 추천"""
    recommended_ids, scores = recommender.get_recommendations(
        selected_idol_ids=request.selected_idol_ids,
        limit=request.limit
    )
    return RecommendResponse(
        recommended_ids=recommended_ids,
        scores=scores
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}