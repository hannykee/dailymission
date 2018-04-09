#0408 자연수를 뒤집어 리스트로 만들기
'''digit_reverse함수는 양의 정수 n을 매개변수로 입력받습니다.
n을 뒤집어 숫자 하나하나를 list로 표현해주세요
예를들어 n이 12345이면 [5,4,3,2,1]을 리턴하면 됩니다.
'''

def digit_reverse(n):
    n_list=[]
    for i in n:
        n_list.append(i)
    n_list.reverse()
    return n_list



n=str(input("숫자열을 입력하세요."))
print(digit_reverse(n))
