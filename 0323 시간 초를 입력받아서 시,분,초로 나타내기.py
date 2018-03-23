#0323 시간 초를 입력받아서 시,분,초로 나타내기

tinput = int(input("시간초를 입력하세요. ex)3400"))

sec = tinput % 60
tinput/=60   #대입연산자 사용하는 이유

min = tinput % 60
tinput/=60

hour=int(tinput)

print("%d시 %d분 %d초입니다." %(hour,min,sec))
