#0321 리스트에서 원하는 값 찾기

numbers = []

while len(numbers) < 5:
    a = int(input("숫자를 입력하세요."))
    numbers.append(a)

obnum=int(input("찾고자 하는 숫자를 입력하세요."))
oblist=[]

for i in range(0,len(numbers)):
    if obnum == numbers[i]:
        oblist.append(i)

print("찾고자 하는 숫자의 위치 값 :",oblist)
#중복위치 고려 
