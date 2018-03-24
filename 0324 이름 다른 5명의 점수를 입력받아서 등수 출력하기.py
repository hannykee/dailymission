#0324 5명의 점수를 입력받아서 등수 출력하기

name_score={}

for n in range (0,5):
    a=str(input("이름,점수를 입력하세요. 예:기쁨이,90"))
    b=a.split(",")
    name_score.append(b[0]:b[1])

for k in range(0,len(name_score)):
    order=6
    for m in range(0,len(score)):
        if name_score[k번째 키값] >= score[m번째 키값]:
            order-=1
    print("%d번째 선수의 점수는 %s이고, 등수는 %d등 입니다." %(k+1,name_score[k번째 키값],order))
