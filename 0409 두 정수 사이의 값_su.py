#0409 두 정수 사이의 합
'''
adder함수는 정수 a, b를 매개변수로 입력받습니다.
두 수와 두 수 사이에 있는 모든 정수를 더해서 리턴하도록 함수를 완성하세요. a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
예를들어 a가 3, b가 5이면 12를 리턴하면 됩니다.

a, b는 음수나 0, 양수일 수 있으며 둘의 대소 관계도 정해져 있지 않습니다.
'''

def adder(a,b):
    p=min(a,b)  #대소관계 비교
    q=max(a,b)
    c=0
    for i in range(p,q+1):
        c+=i
    return c


a=int(input("정수 입력"))
b=int(input("정수 입력"))
print(adder(a,b))
