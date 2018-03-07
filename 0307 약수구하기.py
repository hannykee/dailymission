#0307 약수구하기
num=int(input("숫자를 하나 입력하세요: "))

divisiors=[]

t_num=int(num/2)

while t_num > 1 :
    if num % t_num == 0 :        
        divisiors.append(t_num)
        t_num -=1 #1씩 줄어드는 것을 쉽게 표현하기 위한 대입연산자
#for문으로 범위 설정 다시 연습해보기

print("약수목록 : ", divisiors)
