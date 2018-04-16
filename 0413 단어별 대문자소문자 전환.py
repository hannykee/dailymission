#0413 이상한 문자 만들기
'''toWeirdCase함수는 문자열 s를 매개변수로 입력받습니다.
문자열 s에 각 단어의 짝수번째 인덱스 문자는 대문자로, 홀수번째 인덱스 문자는 소문자로 바꾼 문자열을 리턴하도록 함수를 완성하세요.
예를 들어 s가 try hello world라면 첫 번째 단어는 TrY, 두 번째 단어는 HeLlO, 세 번째 단어는 WoRlD로 바꿔 TrY HeLlO WoRlD를 리턴하면 됩니다.
주의 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단합니다.'''


def toWeirdCase(s):
    weird=[]
    for i in s:
        word=str(i)
        trans=""
        for j in range(0,len(word)):
            if j%2!=0:
                c=word[j].upper()
                trans+=c
            else:
                c=word[j].lower()
                trans+=c
        weird.append(trans)
    return weird


s=str(input("문자열을 입력하세요."))
s=s.split(" ")
print("이상한 문자열은 : ",toWeirdCase(s))
