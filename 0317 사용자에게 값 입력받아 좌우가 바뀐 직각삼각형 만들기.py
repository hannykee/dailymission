#0317 사용자에게 값 입력받아 좌우가 바뀐 직각삼각형 만들기

width = int(input("직각삼각형의 밑변의 길이를 입력하세요."))

j=1
for i in range(1, width+1):
	print(" " * (width-i), "*" * j)
	j+=1
