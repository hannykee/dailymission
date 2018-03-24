#0324 5명의 점수를 입력받아서 등수 출력하기

score=[]

while len(score)<5:
    a=int(input("점수를 입력하세요"))
    score.append(a)


for k in range(0,len(score)):
    order=6
    for m in range(0,len(score)):
        if score[k] >= score[m]:
            order-=1
    print("%d번째 선수의 점수는 %s이고, 등수는 %d등 입니다." %(k+1,score[k],order))
