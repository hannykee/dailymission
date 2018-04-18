#0418 점프 투 파이썬 연습문제 1-Q1
#주민등록번호 연월일부분과 그 뒤의 숫자 부분으로 나누기(문자열 슬라이싱)
#변형) 성별만 남기고 나머지 block처리, 각 변수 데이터에 저장

def slicing(pin):
    yymmdd=pin[0:5]
    num=pin[8:]
    print("생년월일 : ",yymmdd)
    if num[0]==2 or num[0]==4:
        print("여성")
    else:
        print("남성")

def block(pin):
    pin[1:]='*'##이거 for문 없이 하는 법 뭘까
    return pin


pin=str(input("주민등록번호를 입력하세요."))
slicing(pin)
print(block(pin))
