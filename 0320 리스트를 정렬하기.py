#0320 리스트를 정렬하기
#사용자에게 여러 숫자를 입력받은 후 오름차순으로 정렬해서 출력하기

numlist = []

while len(numlist) < 5 :
    t_num = int(input("숫자를 입력하세요 : "))
    numlist.append(t_num)
    
for i in range(0,5):
    for j in range(0,len(numlist)):
        if numlist[i] 
