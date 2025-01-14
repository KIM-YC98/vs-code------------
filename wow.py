# Q
# 그만하시겠습니까? yes 인 경우 종료합니다.
# 그만하시겠습니까? no 인 경우 다시 입력을 받습니다.

class Grade:
    def __init__(self,kor,eng,math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def get_total(self):
        return self.kor + self.eng + self.math

    def get_avg(self):
        return self.get_total() / 3

    def get_grade(self):

        avg = self.get_avg()
        grade = "가"

        if avg >= 90:
            grade = '수'
        elif avg >= 80:
            grade = '우'
        elif avg >= 70:
            grade = '미'
        elif avg >= 60:
            grade = '양'
        else:
            grade ='가'

        return grade


def main():
    kor = int(input("국어 점수 입력 : "))
    eng = int(input("영어 점수 입력 : "))
    math = int(input("수학 점수 입력 : "))

    grade = Grade(kor,eng,math)

    print("총점 : ",grade.get_total())
    print("평균 : ",grade.get_avg())
    print("학점 : ",grade.get_grade())


main() # 시작점이라는 의미가 있다.

# 안 좋은 예시
while True:
    yn = input("그만하시겠습니까? ")
    if yn == 'yes':
        break
    elif yn == 'no':
        main()
    else:
        print("yes 또는 no로 입력해주세요.")
        continue






   # 좋은 예시
   # kor = int(input("국어 점수 입력 : "))
   # eng = int(input("영어 점수 입력 : "))
   # math = int(input("수학 점수 입력 : "))

   # grade = Grade(kor,eng,math)

   # print("총점 : ",grade.get_total())
   # print("평균 : ",grade.get_avg())
   # print("학점 : ",grade.get_grade())
   # cintinue_yn = input("계속하시겠습니까? (y/n) ")
   # if continue_yn.upper() != 'Y' and continue_yn.upper() != 'YES':
   # break
   # print("프로그램 종료")