#0323 등수 다른 풀이 방법

scores=[]
while not len(score)==5:
    score=int(input("점수를 입력하세요: "))
    scores.append(score)

seq=0
for s in scores:
    seq+=1 #몇번째학생
    rank=1
    for ss in scores:
        if s <ss:
            rank +=1
        print("%d번째 선수의 점수는 %d점이고, 등수는 %d등 입니다." %(seq,s,ss))
