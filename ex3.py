def get_mbti_type():
    extroversion_score = 0
    sensing_score = 0
    thinking_score = 0
    judging_score = 0

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

    # '결정 방식'에 대한 질문
    answer = input("문제를 해결할 때 논리적인 분석과 객관적인 판단에 의존하는 편인가요? (예/아니오): ")
    if answer.lower() == "예":
        thinking_score += 1

    answer = input("다른 사람들의 감정과 가치를 고려하여 결정하는 편인가요? (예/아니오): ")
    if answer.lower() == "아니오":
        thinking_score += 1

    answer = input("친구에게 조언을 하는 것을 좋아하는가요? (예/아니오): ")
    if answer.lower() == "예":
        thinking_score += 1

    # '생활 방식'에 대한 질문
    answer = input("계획을 세우고 선호하는 편인가요? (예/아니오): ")
    if answer.lower() == "예":
        judging_score += 1

    answer = input("유연하게 일하는 것을 선호하는 편인가요? (예/아니오): ")
if answer.lower() == "아니오":
        judging_score += 1

answer = input("계획이 수틀리면 스트레스를 받나요? (예/아니오): ")
if answer.lower() == "예":
    judging_score += 1


# 'E/I' 결과 계산
ei_result = "E" if extroversion_score >= 2 else "I"

# 'S/N' 결과 계산
sn_result = "S" if sensing_score >= 2 else "N"

# 'T/F' 결과 계산
tf_result = "T" if thinking_score >= 2 else "F"

# 'J/P' 결과 계산
jp_result = "J" if judging_score >= 2 else "P"

return ei_result + sn_result + tf_result + jp_result

# 출력 오류남!!!!!!

# MBTI 유형 획득
mbti_type = get_mbti_type()
print("당신의 MBTI 유형은:", mbti_type)        