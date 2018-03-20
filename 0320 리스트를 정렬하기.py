#0320 리스트를 정렬하기
#사용자에게 여러 숫자를 입력받은 후 오름차순으로 정렬해서 출력하기

numlist = []

while len(numlist) < 5 :
    t_num = int(input("숫자를 입력하세요 : "))
    numlist.append(t_num)

    
#TIP) list도 len 사용하여 길이 파악할 수 있다!!
    
for i in range(0,len(numlist)):
    for j in range(0,len(numlist)):
        if numlist[i] < numlist[j]:
            orderchange = numlist[i]
            numlist[i] = numlist[j]
            numlist[j] = orderchange
            #순서를 바꿀 뿐 변수를 없애지 않는 방법!! 매우 중요!!
print(numlist)
#중첩문에서 구조 내 반복 순서 중요!!
