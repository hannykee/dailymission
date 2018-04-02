#0402 문자열 함수 나열 - 점프 2 python


"%10sjane" % 'hi'   #공백주고 오른쪽 정렬

"-10sjain" %'hi'    #공백주고 왼쪽 정렬


#소수점 표현 (자리수 설정)

"%0.4f" %3.42134234
"%10.4f" %3.42134234


#문자 개수 세기 <count>
a= hobby
a.count('b')

#위치 알려주기<find>
a= "Python is easy"
a.find('y') #가장 처음 나온 위치를 반환한다!!! 매우 중요
           #단, 없으면 -1을 반환함.

#위치 알려주기<index>
a= "My life is wonderful"
a.index('l')
            #단, 없으면 오류 반환

#문자열 삽입 <join>
a=","
a.join('abcd')

#소문자 대문자로 <upper> , 반대는 lower
a.upper()
a.lower()

#왼쪽 공백 지우기
a.lstrip()
#오른쪽 공백 지우기
a.rstrip()
#양쪽 공백 지우기
a.strip()

#문자열 바꾸기
a.replace("원래","바꿀것")

#문자열 나누기
a.split() #값 안넣으면 공백이나 엔터 기준으로 분리
a.split("나눌기준,나 : 같은 것")


#고급 포매팅 기술 존재 https://wikidocs.net/13을 보고 연습함.
