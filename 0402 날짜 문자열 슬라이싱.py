#0402 파이썬 슬라이싱(날짜정보 문자열 나누기)

a= "20180402Sunny"
year=a[0:4] #슬라이싱에서 끝번호는 해당 안됨 0 <= a < 5
month=a[4:6]
day=a[6:8]
weather=a[8:]

print("오늘은 %s,%s,%s,%s 입니다" %(year,month,day,weather))
#포매팅 문자열은 s 정수형은 d 실수는 f    %만 표현할 때는 %%
