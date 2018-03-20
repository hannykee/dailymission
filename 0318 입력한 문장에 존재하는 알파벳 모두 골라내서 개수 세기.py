#0318 입력한 문장에 존재하는 알파벳 모두 골라내서 개수 세기

userstr = str(input("문장을 입력하세요."))
str0 = userstr.replace(' ','')

dicuser = {}

for i in str0:
	for j in dicuser.keys():    #딕셔너리 키 값에 접근하는 방식 주의!
		if i!=j:
			dicuser[j]=1
		if i==j: 
			dicuser[j]+=1 ##사용 방식 주의! +=대입 연산자 사용했네~ 반대로도 해보기.

print(dicuser)

			
			
