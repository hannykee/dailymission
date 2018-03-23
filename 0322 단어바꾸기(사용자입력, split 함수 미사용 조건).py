#0323 단어바꾸기(사용자입력, split 함수 미사용 조건)

x0= str(input("문장을 입력하세요."))

word = ""    #변수
string = []  #리스트 차이 유의

#0318확인 i가 아니라 쓸 때 숫자(범위)로 설정되어 있으니까 x0[i]


for i in range(0,len(x0)):
	if x0[i]!=" ":   # 공백 을 나타낼 때 참고
		word += x0[i]   #문자열도 연산 가능(나열해서 붙이기)
		if i == len(x0)-1:  #왜 여기에서 -1을 하지? 파이썬 특징! 마지막 숫자가 +1이니까
			string.append(word)
	else:
		string.append(word)
		word="" #변수 초기화

finalstr=""
for k in range(0,len(string)):
        if string[k]=="어려워요":
                string[k]="쉬워요"

        if k != len(string)-1:
                finalstr += string[k] + " "
        else:
                finalstr += string[k]
	
print(finalstr)
