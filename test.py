string = str(input("문장을 입력하세요: "))
a=[]

for i in string:
    exist = False
    for j in range(0, len(a)):
        if i == a[j]:
            exist=True
            break
        if not exist:
            a.append(i)

print(a)
