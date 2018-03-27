#0325 핸드폰 번호 가리기


def hide_numbers():
        p_num=str(input("번호를 입력하세요."))
        rawdata= p_num[-4:]
        blockdata= "*" * (len(p_num)-4)

        return blockdata+rawdata
                  

"""왜냐하면 문자열의 요소값은 바꿀 수 있는 값이 아니기 때문이다
(문자열, 튜플 등 의 자료형은 그 요소값을 변경할 수 없다.
그래서 immutable한 자료형이라고도 부른다).
하지만 앞서 살펴본 슬라이싱 기법을 이용하면 "Pithon"이라는 문자열을
"Python"으로 바꿀 수 있는 방법이 있다.-책 참고"""
#        number=p_num.split("-")
	

print("결과 : " , hide_numbers())



