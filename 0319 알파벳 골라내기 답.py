#0319 알파벳 골라내기 답
string = str(input("문장을 입력하세요 : "))

alphas = []

for i in string:
    exsit=False
    for j in range(0,len(alphas)):
        if i==alphas[j]:
            exist=True
            break
    if not exsit :
        alphas.append(i)
            
print(alphas)
