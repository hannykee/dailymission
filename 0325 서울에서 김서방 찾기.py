#0325 서울에서 김서방 찾기

#findKim 함수(메소드)는 String형 배열 seoul을 매개변수로 받습니다.

#seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하세요.
#seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.


seoul=["Park","Lee","Bae","Kim","Yoon"]

def findKim(seoul):
	loc=seoul.index("Kim")
	return loc

print("서울에서 김 서방 위치는 : ",findKim(seoul))
