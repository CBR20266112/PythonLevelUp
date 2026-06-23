# Quiz) 월 15회 사먹는데 4번은 외식 11번은 배달로 하기로 했다.
from random import * # 아 라이브러리 수입해오기 자꾸 까먹어.
print(int(random() *30)) # 삭망월 빼곤 그냥 적당히 30일까지인 걸로 쳐.
# 자 근데 매달 1일은 돈 오가는 날이라 좀 사려야 돼.
print(randrange(2, 31)) # rnadrange는 속괄호 안에 수를 채워줘야 돼.
# 변수를 이용해서 문장 구성을 쉽게 해보자.
deliverate = randint(2, 30) 
# 출력
print("배달 시켜먹고 싶어?",str(deliverate)+"일까진 좀 참아 봐.")