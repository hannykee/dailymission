#0325 핸드폰 번호 가리기

def hide_numbers():
	p_num= str(input("핸드폰 번호를 입력해주세요."))
	for i in range(0,len(p_num)-4):
		p_num[i]="*"
	return p_num

print("결과 : " + hide_numbers())
