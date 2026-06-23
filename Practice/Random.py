# 난수..
from random import *
# from이 라이브러리 끌어다 오는 #include 같은 역할인 건가?
print(random()) # 0.0 ~ 1.0 미만의 임의 값 생성.
print(random() *10) # 자릿수 하나 증가시키기.
# 소수점 없애보기.
print(int(random() *10)) # 정수형으로.
print(int(random() *10) +1) # 위 값에 +1?
# 로또 번호 추첨?
print(int(random() *45) +1) # 로또남바 하나 추첨, 그런데 아직 5개 더..
# 그런데 간략화된 명령어가 있대.
print(randrange(1, 46)) 
print(randrange(1, 46)) 
print(randrange(1, 46)) 
print(randrange(1, 46)) 
print(randrange(1, 46))
# 또 다른 변형.
print(randint(1, 45)) # 얘는 양 끝 수도 포함하는 거래.