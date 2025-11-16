# 그룹별 메타데이터 (수동 관리)
GROUP_METADATA = {
    "엔하이픈": {
        "agency": "빌리프랩",
        "genres": ["K-POP", "팝", "댄스", "록", "R&B", "EDM", "랩/힙합"],
        "description": "대한민국의 남자 아이돌 그룹이며, 빌리프랩 소속이고, 주요 장르는 K-POP, 팝, 댄스, 록, R&B, EDM, 랩/힙합입니다."
    },
    "블랙핑크": {
        "agency": "YG",
        "genres": ["댄스", "랩/힙합", "팝", "R&B/Soul", "록/메탈", "포크/블루스", "EDM/뭄바톤"],
        "description": "대한민국의 여자 아이돌 그룹이며, YG 소속이고, 주요 장르는 댄스, 랩/힙합, 팝, R&B/Soul, 록/메탈, 포크/블루스, EDM/뭄바톤입니다."
    },
    "에스파": {
        "agency": "SM",
        "genres": ["K-POP", "댄스", "힙합", "하이퍼팝", "발라드"],
        "description": "대한민국의 여자 아이돌 그룹이며, SM 소속이고, 주요 장르는 K-POP, 댄스, 힙합, 하이퍼팝, 발라드입니다."
    },
    "아이브": {
        "agency": "스타쉽",
        "genres": ["댄스", "팝", "EDM", "R&B", "힙합", "발라드"],
        "description": "대한민국의 여자 아이돌 그룹이며, 스타쉽 소속이고, 주요 장르는 댄스, 팝, EDM, R&B, 힙합, 발라드입니다."
    },
    "라이즈": {
        "agency": "SM",
        "genres": ["이모셔널팝"],
        "description": "대한민국의 남자 아이돌 그룹이며, SM 소속이고, 주요 장르는 이모셔널팝입니다."
    },
    "아스트로": {
        "agency": "판타지오",
        "genres": ["댄스", "발라드"],
        "description": "대한민국의 남자 아이돌 그룹이며, 판타지오 소속이고, 주요 장르는 댄스, 발라드입니다."
    },
}


def get_group_description(group_name: str) -> str:
    """그룹 이름으로 메타데이터 설명 가져오기"""
    metadata = GROUP_METADATA.get(group_name, None)
    if metadata:
        return metadata["description"]
    return ""  # 메타데이터 없으면 빈 문자열

