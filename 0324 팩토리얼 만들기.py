#0324 팩토리얼 만들기(1부터 주어진 숫자까지의 곱)

x=int(input("x!에서 x를 숫자로 입력하세요."))

fac=1

while not x==1:
    fac *= x
    x -= 1
print(fac)
