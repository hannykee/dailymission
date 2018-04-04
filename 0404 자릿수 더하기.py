#0404 자릿수더하기
'''sum_digit함수는 자연수를 전달 받아서 숫자의 각 자릿수의 합을 구해서 return합니다.
예를들어 number = 123이면 1 + 2 + 3 = 6을 return하면 됩니다.
sum_digit함수를 완성해보세요.'''

def sum_digit(n):
    b=0
    for i in range(0,len(n)):
        a=int(n[i])
        b+=a

    return b



n=str(input("자연수를 입력하세요. ex)123"))
print("결과: ", sum_digit(n))
