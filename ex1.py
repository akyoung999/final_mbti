def mbti_question_1():
    answer = input("다른 사람들과 함께 시간을 보내는 것에 에너지를 얻나요? (예/아니오): ")
    if answer.lower() == "예":
        return 1
    elif answer.lower() == "아니오":
        return 0
    else:
        print("유효한 답변이 아닙니다.")
        return mbti_question_1()

def mbti_question_2():
    answer = input("혼자만의 시간을 갖는 것에 에너지를 얻나요? (예/아니오): ")
    if answer.lower() == "예":
        return 0
    elif answer.lower() == "아니오":
        return 1
    else:
        print("유효한 답변이 아닙니다.")
        return mbti_question_2()

# 추가 질문 3
def mbti_question_3():
    answer = input("친구들과 함께 있지 않으면 외로운가요? (예/아니오): ")
    if answer.lower() == "예":
        return 1
    elif answer.lower() == "아니오":
        return 2
    else:
        print("유효한 답변이 아닙니다.")
        return mbti_question_3()

def get_mbti_type():
    extroversion = mbti_question_1() + mbti_question_2() + mbti_question_3()

    mbti_type = "E" if extroversion >= 2 else "I"

    return mbti_type

# MBTI 유형 획득
my_mbti = get_mbti_type()
print("당신의 MBTI 유형은:", my_mbti)
