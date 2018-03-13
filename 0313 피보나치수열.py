#0313 피보나치수열

num = int(input("출력하고 싶은 값의 개수를 입력하세요"))

fibo = [0,1] #피보나치 수열은 0과 1부터 시작되므로 미리 리스트에 0,1 넣어둠


for i in range(2,num):
    f1=fibo[i-2]
    f2=fibo[i-1]
    fibo.append(f1+f2)

#바로 이렇게 해도 되지만 print(fibo)
    #그 값을 하나하나 출력하고 싶은 경우

for f in fibo:
    print(f)


#매우 헷갈리던 부분! 리스트에서 그 값을 하나하나 찍어주고 싶을 경우
    #for 문을 사용하여 fibo리스트 안에 임의의 인자 f로 설정하고 f를 출력 명령
