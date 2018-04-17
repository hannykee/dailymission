#0415 복권 당첨 번호 만들기

import random


my_numbers=[]
for num in range(0,6):
	my_numbers.append(random.randrange(0,45))
my_bonus=random.randrange(0,45)

print("당신이 선택한 번호는 ", my_numbers, " + ", my_bonus,"입니다.")


numbers=[]

for num in range(0,6):
	numbers.append(random.randrange(0,45))
bonus=random.randrange(0,45)

print("당첨번호는", numbers, " + ",bonus,"입니다.")


#당첨확인
count=0
for i in my_numbers:
	for j in numbers:
		if i == j:
			count+=1
			break

if count==6:
	print("1등 당첨")
elif count==5 and (bonus==my_bonus):
	print("2등 당첨")
elif count==5 and (bonus!=my_bonus):
	print("3등 당첨")
elif count==4:
	print("4등 당첨")
elif count==3:
	print("5등 당첨")
else: 
	print("꽝! 다음 기회에")
