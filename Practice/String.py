# 문자열
python = "So Hard" # 대.소문자 혼합되어 있음.
print(python.lower())
# lower는 싺 다 소문자행. 그럼 upper는?
print(python.upper())
# 대문자인지 확인하는 구문도 있대.
print(python[0].isupper())
# 그럼 이건 첫 번째 글자가 소문자인지 확인하는 거고.
print(python[0].islower()) # 왜냐면 So는 대문자로 시작했잖아.
# 이건 문장 길이 확인이래. 뭔가 좀 요긴할 듯.
print(len(python)) # 띄어쓰기까지 총 7자인 거지.
A = "ImTheKoreanTopClassHiphopMobeomNoblessFabulousTurbulenceGorgeousButDangerous"
print(len(A))
# 글자 대체해 보기. 재밌겠다.
print(python.replace("Hard", "Difficult"))
print(python.replace("So", "Over My head"))
# 특정글자만 찝어오기.
index = python.index("S") # 인덱스로 글자 찝어올 땐 대소문자까지 명확힉 해줘야 하네,
print(index)
# 그 다음다음 s를 찾아오는 거야. 3번째 s를 찾아오는 거니까, Noble's's
index2 = A.index("s")
index3 = A.index("s", index2 + 2)
print(index3)
# 글자 찾아와.
print(A.find("D"))
PRINT()