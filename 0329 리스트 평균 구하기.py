#20180329  평균구하기
'''
함수를 완성해서 매개변수 array의 평균값을 return하도록 만들어 보세요.
어떠한 크기의 array가 와도 평균값을 구할 수 있어야 합니다.
'''

def sumfunc ():
    a= input("평균을 구할 숫자들을 입력하세요. ex) 4,10")
    a= a.replace(" ","")
    numlist=a.split(",")

    sum_list=0
    for i in numlist:
        sum_list += int(i)

    mean= sum_list / len(numlist)
    return mean


print("평균 값은 : ", sumfunc())
