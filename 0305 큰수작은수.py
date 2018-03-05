#3월 5일 미션: 두 숫자 중에서 큰 숫자에서 작은 숫자를 뺀 값 출력하기

#함수

#변수
num1, num2 = "",""

#실행코드
num1= int(input("첫 번째 숫자를 입력하세요"))
num2= int(input("두 번째 숫자를 입력하세요"))

if num1> num2:
    print (num1-num2)
else:
    print (num2-num1)
