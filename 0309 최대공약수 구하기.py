#03-09 최대공약수 구하기

num1 = int(input("첫 번째 수를 입력하세요"))
num2 = int(input("두 번째 수를 입력하세요"))

t_num = 0

if num1 > num2:
    t_num=num2
else :
    t_num=num1
    

while t_num > 1:
    if num1%t_num==0 and num2%t_num==0:   #틀린 부분: 나눴을 때 0이 되는건 비정상, 나머지가 0이 되어야 한다. 나머지 기호 주의!!
        print("최대공약수는 : %d 입니다." %t_num) #d 정수, s 문자 기호 %주의
        break
    t_num -= 1
        
