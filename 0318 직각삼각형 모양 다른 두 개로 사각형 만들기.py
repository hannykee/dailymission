#0318 직각삼각형 모양 다른 두 개로 사각형 만들기

width=int(input("직각삼각형 밑변의 길이를 입력하세요."))
width1=width

for i in range(1,width+1):
	while width1 > 0 :
		print('*' * i, '@' * width1)
		width1-=1
		break

#테스트용 실제로 파이썬에서 돌아가는지 확인하자!
