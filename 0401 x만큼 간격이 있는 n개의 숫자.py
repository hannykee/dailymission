#0401 x만큼 간격이 있는 n개의 숫자
'''
number_generator함수는 x와 n을 입력 받습니다.
2와 5를 입력 받으면 2부터 시작해서 2씩 증가하는 숫자를 5개 가지는 리스트를 만들어서 리턴합니다.
[2,4,6,8,10]

4와 3을 입력 받으면 4부터 시작해서 4씩 증가하는 숫자를 3개 가지는 리스트를 만들어서 리턴합니다.
[4,8,12]

이를 일반화 하면 x부터 시작해서 x씩 증가하는 숫자를 n개 가지는 리스트를 리턴하도록 함수 number_generator를 완성하면 됩니다.
'''



def number_generator(x,n):
    num_list=[]
    for i in range(x,(x*n)+1,x):
        num_list.append(i)
    return num_list



x=int(input("시작 위치와, 증가 폭을 숫자로 입력하세요."))
n=int(input("반복할 횟수를 입력하세요."))

number_generater(x,n)
