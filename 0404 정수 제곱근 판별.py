#0404 정수 제곱근 판별하기

'''nextSqaure함수는 정수 n을 매개변수로 입력받습니다.
n이 임의의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고,
n이 임의의 정수 x의 제곱이 아니라면 'no'을 리턴하는 함수를 완성하세요.
예를들어 n이 121이라면 이는 정수 11의 제곱이므로
(11+1)의 제곱인 144를 리턴하고, 3이라면 'no'을 리턴하면 됩니다.'''

def nextSquare(n):
    for i in range(1,10):
        if n % (i**2)==0:
            return (n+1)**2
            break
        else:
            return 'no'





n= int(input("정수를 입력하세요."))

print("x의 제곱근: ",nextSquare(n))
