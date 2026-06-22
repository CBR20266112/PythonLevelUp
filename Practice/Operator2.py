# Not연산인 듯.
print(1 != 5)
print(not(1 != 5))
print(not(1 == 5))
# 이건 And인 듯.
print((3 > 0) and (3 < 5))
print((18 > 2) & (3 < 5))
print((2 > 1) & (1 == 0))
# Or 연산도 있지.
print((3 > 0) or (3 < 5))
print((18 > 2) | (3 < 5))
print((2 > 1) | (1 == 0))
# 괄호 안에 아가리 3개.
print((3 > 2 < 5))
print((3 > 2 > 5))