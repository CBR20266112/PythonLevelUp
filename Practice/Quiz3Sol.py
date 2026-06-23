# 퀴즈. 다시해!!! 멍청아!!!!!!!!!!!
url = "https://www.google.com" # 일단 사이트 주소.
my_url = url.replace("https://www.", "") # 아 아예 앞부분을 생략시키는 걸로?
print(my_url)
my_uurl = my_url[:my_url.index(".")] # my_url에서 .을 찾고 그것부터는 잘라버리는 거래.
print(my_uurl)
pw = my_url[:3] + str(len(my_uurl)) + str(my_url.count("e")) + "!"
# 문자형은 또 그때마다 str 붙여줘야 하니 너무 귀찮고 번거롭다.
print("{}의 비밀번호는 {}입니다.".format(url, pw))
print("\"네 개인정보 대공개\"")
# 변형
url = "https://www.daum.net"
my_url = url.replace("https://www.", "")
my_uurl = my_url[:my_url.index(".")]
print(my_uurl)
pw = my_url[:3] + str(len(my_uurl)) + str(my_url.count("e")) + "!"
print("{}의 비밀번호는 {}입니다.".format(url, pw))