#0413  대문자 소문자 제목
'''Jaden_Case함수는 문자열 s을 매개변수로 입력받습니다.
s에 모든 단어의 첫 알파벳이 대문자이고, 그 외의 알파벳은 소문자인 문자열을 리턴하도록 함수를 완성하세요
예를들어 s가 3people unFollowed me for the last week라면 3people Unfollowed Me For The Last Week를 리턴하면 됩니다.'''

def Jaden_Case(s):
	s=s.title()
	return s
	

s=str(input("문자열을 입력하세요."))
print("출력 문자열은 : ",Jaden_Case(s))
