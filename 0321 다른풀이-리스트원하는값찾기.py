#0321 다른 풀이 방법- 리스트 원하는 값 찾기

numbers = []
while not len(numbers)==5:
    t_n = int(input("숫자를 입력하세요."))
    numbers.append(t_n)

f_num = int(input("찾으실 숫자를 입력하세요."))

idx=-1

for i in range(0,len(numbers)):
    if numbers[i] == f_num:
        idx=i

if idx== -1:
    print("요소가 존재하지 않습니다.")
else:
    print("찾으시는 요소가 %d번 위치에 있습니다." %idx)
