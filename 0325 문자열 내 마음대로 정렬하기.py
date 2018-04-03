#0325 문자열 내 마음대로 정렬하기
#strange_sort함수는 strings와 n이라는 매개변수를 받아들입니다.
#strings는 문자열로 구성된 리스트인데, 각 문자열을 인덱스 n인 글자를 기준으로 정렬하면 됩니다.

#예를들어 strings가 [sun, bed, car]이고 n이 1이면 각 단어의 인덱스 1인 문자 u, e ,a를 기준으로 정렬해야 하므로 결과는 [car, bed, sun]이 됩니다.
#strange_sort함수를 완성해 보세요


def strange_sort(strings,n) :
        
        strings.sort(key=str.lower)
        print(strings)
        return strings

a=str(input("원하는 문자열을 나열하여 입력하세요."))
a=a.replace(" ","")
strings=a.split(",")  #split은 list로 반환
n=int(input("원하는 인덱스를 설정하세요."))
strange_sort(strings,n)




#https://wayhome25.github.io/python/2017/03/07/key-function/ 딕셔너리 정렬 키 값 설정하기
#본문 https://docs.python.org/3/howto/sorting.html?highlight=sorting#key-functions

#iterable 정의 http://bluese05.tistory.com/55
