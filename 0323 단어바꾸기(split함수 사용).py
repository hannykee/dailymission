#0323 단어바꾸기(split사용)

userstr= str(input("문장을 입력하세요."))

wlist= userstr.split(" ")   # split 함수 문법 중요!!

resultstr=""

for i in range(0,len(wlist)):
    if wlist[i]=="어려워요":
        wlist[i]="쉬워요"
    if i!= len(wlist)-1:
        resultstr+=wlist[i]+" "

    else:
        resultstr+=wlist[i]
        print(resultstr)
        break
