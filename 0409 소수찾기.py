#0409 소수찾기

'''
numberOfPrime 메소드는 정수 n을 매개변수로 입력받습니다.
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하도록
numberOfPrime 메소드를 만들어 보세요.
소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)
10을 입력받았다면, 1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환
5를 입력받았다면, 1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환
'''

def numberOfPrime(n):
    num_list=[]
    for i in range(2,n+1):
        count=0
        for j in range(2,i):
            if i%j==0:
                count+=1
        if count==0:
            num_list.append(i)
    p_num=len(num_list)
    print(num_list)
    return p_num
n=int(input("정수입력"))
print(numberOfPrime(n))
