#0318 입력한 문장에 존재하는 알파벳 모두 골라내기(중복 x)

userstr = str(input("원하는 문장을 입력하세요."))  ##중요 : 문자열로 취급 str()
str0 = userstr.replace(' ','')

alphabet = []   #<주의!!!> 빈 리스트 만들기는 [] , 빈 문자열 변수 만들기가 "" 

for i in str0:
    for j in range(0,len(alphabet)):
        if i != alphabet(j):
            alphabet.append(i)
        else:
            break


print("입력한 알파벳 : ",alphabet)

#공백제거 함수 뭐였지? 답:https://code.i-harness.com/ko/q/7e310c

#길이 출력하는 함수!! len(변수)
