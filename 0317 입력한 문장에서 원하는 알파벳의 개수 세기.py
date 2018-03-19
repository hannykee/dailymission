#0317 입력한 문장에서 원하는 알파벳의 개수 세기

userstr= str(input("문장을 입력해주세요.")) #str () 함수 문자열로 인식!! 중요
usertarget=str(input("찾을 알파벳(단일문자)을 입력해주세요."))

count=0

for i in userstr:
	if i==usertarget:  ##userstr[i]로 하면 아마도 에러날 걸! 정확히는 i 이다. 범위조건에서 이미 해당, 그리고 값다는 등호는 =가 아니라 ==이다.
			# 뭐지 근데 해보니까 오류 안난다..
		count=count+1

print("%s 의 개수는 %s 개 입니다." %(usertarget,count))
