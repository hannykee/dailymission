#0408 제일 작은 수 제거하기

def rm_small(b):
    c=min(b)
    b.remove(c)
    return b

mylist=str(input("숫자리스트를 입력하세요."))
a=mylist.replace(" ","")
b=a.split(",")  #너는 변수를 소중히 하지 않았지.
print(type(b))  #타입 확인 명령어! 

print(rm_small(b))
