def get_mbti_type():
    extroversion_score = 0
    sensing_score = 0

    # '선호하는 세계'에 대한 질문
    answer = input("다른 사람들과 함께 시간을 보내는 것에 에너지를 얻나요? (예/아니오): ")
    if answer.lower() == "예":
        extroversion_score += 1

    answer = input("혼자만의 시간을 갖는 것에 에너지를 얻나요? (예/아니오): ")
    if answer.lower() == "아니오":
        extroversion_score += 1

    answer = input("친구들과 함께 있지 않으면 외로운가요? (예/아니오): ")
    if answer.lower() == "예":
        extroversion_score += 1

    # '정보 수집 방식'에 대한 질문
    answer = input("세부사항에 주목하고 구체적인 정보를 선호하나요? (예/아니오): ")
    if answer.lower() == "예":
        sensing_score += 1

    answer = input("큰 그림을 그리고 추상적인 아이디어에 주목하는 편인가요? (예/아니오): ")
    if answer.lower() == "아니오":
        sensing_score += 1

    answer = input("경험을 중점적으로 생각하고 판단을 내리는가요? (예/아니오): ")
    if answer.lower() == "예":
        sensing_score += 1

    mbti_type = ""
    if extroversion_score >= 2:
        mbti_type += "E"
    else:
        mbti_type += "I"

    if sensing_score >= 2:
        mbti_type += "S"
    else:
        mbti_type += "N"

    return mbti_type

# MBTI 유형 획득
my_mbti = get_mbti_type()
print("당신의 MBTI 유형은:", my_mbti)