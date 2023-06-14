def mbti_question_1():
    answer = input("다른 사람들과 함께 시간을 보내는 것에 에너지를 얻나요? (예/아니오): ")
    if answer.lower() == "예":
        return "E"  # 외향 (Extroversion)
    elif answer.lower() == "아니오":
        return "I"  # 내향 (Introversion)
    else:
        print("유효한 답변이 아닙니다.")
        return mbti_question_1()

def mbti_question_2():
    answer = input("세부사항에 주목하고 구체적인 정보를 선호하나요? (예/아니오): ")
    if answer.lower() == "예":
        return "S"  # 감각 (Sensing)
    elif answer.lower() == "아니오":
        return "N"  # 직관 (Intuition)
    else:
        print("유효한 답변이 아닙니다.")
        return mbti_question_2()

def mbti_question_3():
    answer = input("문제를 해결할 때 논리적인 분석과 객관적인 판단에 의존하나요? (예/아니오): ")
    if answer.lower() == "예":
        return "T"  # 사고 (Thinking)
    elif answer.lower() == "아니오":
        return "F"  # 감정 (Feeling)
    else:
        print("유효한 답변이 아닙니다.")
        return mbti_question_3()

def mbti_question_4():
    answer = input("계획을 세우고 구조적으로 조직하는 것을 선호하나요? (예/아니오): ")
    if answer.lower() == "예":
        return "J"  # 판단 (Judging)
    elif answer.lower() == "아니오":
        return "P"  # 인식 (Perceiving)
    else:
        print("유효한 답변이 아닙니다.")
        return mbti_question_4()

def get_mbti_type():
    mbti_type = ""
    mbti_type += mbti_question_1()
    mbti_type += mbti_question_2()
    mbti_type += mbti_question_3()
    mbti_type += mbti_question_4()
    return mbti_type

# MBTI 유형 획득
my_mbti = get_mbti_type()
print("당신의 MBTI 유형은:", my_mbti)