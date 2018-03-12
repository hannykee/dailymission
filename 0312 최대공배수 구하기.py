#03/12 최소공배수 구하기

num1= int(input("첫번째 숫자를 입력하세요"))
num2= int(input("두번째 숫자를 입력하세요"))

t_num=0 #변수 정의 먼저 해주고 시작!@

if num1 > num2:
    t_num=num2
else:
    t_num=num1
    
while t_num :   #나는 t_num >1인줄 알았는데, if에서 break가 있으니 반드시 제어 넣지 않아도 됨.
     #여기에서 3의 배수면 3씩 배가 되게 하고 싶다.
    if num1 % t_num==0 and num2 % t_num==0:
        print("최대공배수는 : %d입니다." %t_num) #나누어 떨어지는 것을 나머지가 0으로 표현
        break                      #쉼표 안붙이고 기호 %임을 주
    t_num += 1
##여기에 왜 else구문 안되는지 모르겠다.    else:
##이유는 꼭 If else 구조가 아니더라도 if조건을 만족시키면 바로 끝내도록 하므로



#나의 생각 접근.. 그러나ㅠ
#for i in range(1,50):
#   obj = num1*i
#    if obj = num2 :
#        print("최대공약수는 : ",obj)
#    else :
#        num2=num2*i



#listnum1=[]
#listnum2=[]

#for i in range(1,50):
#    listnum1.append(num1*i)
#    listnum2.append(num2*i)
#    if listnum1==listnum2:
#        print(listnum1)
#        break;


