# 너무 길어지니까 문자열 찾기는 여기서 이어서.
A = "ImTheKoreanTopClassHiphopMobeomNoblessFabulousTurbulenceGorgeousButDangerous"
print(len(A))
# 특정글자만 찝어오기.
# 그 다음다음 s를 찾아오는 거야. 3번째 s를 찾아오는 거니까, Noble's's
index2 = A.index("s")
index3 = A.index("s", index2 + 2)
print(index3)
# 글자 찾아와.
print(A.find("D")) # Dangerous의 'D' 67번째라는 거지. 근데
print(A.find("z")) # z는 이 문장에 없으니까 -1로 출력되는 거다.
''' index일 때에는 아예 프로그램 진행이 안 된다.
print(A.index("z")) '''
# s 일일이 세어보지 말고.
print(A.count("s")) # 많기도 하다.
print(A.count("ous")) # ous를 이용해서 라임 맞추는 데 썼으니까.