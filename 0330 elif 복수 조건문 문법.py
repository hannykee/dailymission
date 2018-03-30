#0330 elif로 다중 조건 판단문  만들기- 점프 투 파이썬 참고

"주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라"

a=input("주머니에 든 것을 나열하세요. ex) paper,cellphone...")
a=a.replace(' ','')
pocket=a.split(",")

card=int(input("카드가 있다면 1, 없으면 0을 입력하세요."))

'''
pocket = ['paper', 'cellphone']
card = 1
'''

if 'money' in pocket:
     print("택시를 타고가라")
elif card: 
     print("택시를 타고가라")
else:
     print("걸어가라")
