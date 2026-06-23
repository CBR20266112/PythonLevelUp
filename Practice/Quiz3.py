# 또 퀴즈요, 해야죠 예... 사이트별 비밀번호 만들기.
gg = "https://www.google.com" # 일단 사이트 주소.
index = gg.index("g") # g가 몇 번째인지 인덱스 찾기.
print(index) # 12번째라고 하니까.
print(gg[12:]) # 12번째부터 출력해봐.
rulee = (gg[12:18]) # 규칙2의 영어 앞부분 찾아오기.
rule2 = len(rulee) # 위 영어의 길이.
rule3 = rulee.find("e") # 규칙3, e의 갯수.
rule1 = (rulee[:2]) # 이러면 처음 3자리.
rule4 = "!" # 규칙 4의 느낌표.
pw = rule1+rule2+rule3+rule4
print(pw)