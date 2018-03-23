#0323 비만도 측정하기

gender=str(input("성별을 입력하세요 M/F"))

h=int(input("키를 입력하세요"))
w=int(input("몸무게를 입력하세요."))
stw=0 #정수형은 0으로 변수 선언
if gender=="M":
    stw=(h-100)*0.9
if gender=="F":
    stw=(h-100)*0.85
           
else:
    print("잘못된 입력값입니다.")

ww=(w-stw)/stw*100
print("당신의 비만도는 %d이고, 표준체중은 %d입니다." %(ww,stw))
