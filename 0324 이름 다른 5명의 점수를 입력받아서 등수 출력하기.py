#0324 5명의 점수를 입력받아서 등수 출력하기(딕셔너리 저장해보기,리스트변환)

name_score={} 
data=[]
name=[]
for n in range (0,5):
    a=str(input("이름,점수를 입력하세요. 예:기쁨이,90"))
    b=a.split(",")
    name_score[(b[0])]=int(b[1]) #딕셔너리 저장해보기
    name.append(b[0]) #리스트 변환
    data.append(int(b[1]))

#참고용  set(name_score) #set은 키 값만 추출해서 {}형태로 가진다.

for k in range(0,5):
    order=6
    for m in range(0,5):
        if data[k] >= data[m]:
            order-=1
    print("%s 선수의 점수는 %d이고, 등수는 %d등 입니다." %(name[k],data[k],order))



#정렬한채로 인쇄하기
#data.sort()
