#딕셔너리 정리

dic = {'name':'pay', 'phone':'0119999','birth':'1118'}

a[2]='b'
del a[2]

#딕셔너리는 인덱싱 사용 불가

#키값 추출을 리스트로 변환
a.keys()
list(a.keys())

#리스트로 변환안하면 고유 함수 사용안함.
for k in a.keys():
    print(k)

#value값 추출
a.values()
list(a.values())

#get(x) 함수는 x라는 key에 대응되는 value를 돌려준다. 앞서 살펴보았듯이 a.get('name')은 a['name']을 사용했을 때와 동일한 결과값을 돌려받는다.
#None을 리턴

#key,value쌍 얻기
a.items()

#key value 쌍 모두 지우기
a.clear()

#key로 value얻기(get)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
a.get('name')

#딕셔너리 안에 key값이 없을 경우 정해둔 값을 보여주기
a.get('foo', 'bar')

#해당 key가 딕셔너리 안에 있는지 조사하기
'name' in a
True

