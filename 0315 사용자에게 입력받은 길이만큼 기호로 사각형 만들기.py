#0315 사용자에게 값 입력받아 *기호로 사각형 만들기(가로 길이, 세로길이)

width = int(input("가로 길이를 입력해주세요."))
height = int(input("세로 길이를 입력해주세요."))
print('*' * width)
for i in range(0,height-1):
    print('*' * width)

###반복문 구조 매우 중요! 이것도 되네!!!
    #여기에서 i는 반복의 숫자로 설정되고 범위가 0부터 높이 입력값만큼 반복(print명령)의 수를 설정하였다.
