import math  # math 모듈 import
from circle import * # circle.py 모듈로부터 모든 함수와 변수를 가져옴
# import : 모듈 전체를 불러와서 사용할 때 사용
# import : 선언 없이 그냥 언제든 호출 가능한 함수
print("hello")

print(math.pi) # math 모듈의 pi 상수 호출
print(math.sin(5)) # math 모듈의 sin 함수 호출
# 빌트인 함수 : import 선언 없이 언제든 호출 가능한 함수
# 빌트인 모듈 : import 선언 없이 언제든 호출 가능한 모듈
# ex) print(), input(), int(), float(), str(), list(), tuple(), dict(), set(), bool()