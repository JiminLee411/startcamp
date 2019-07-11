#dictionary
# key -value
# key : string, integer, float, boolean 가능
# list, dictionary는 key가 될 수 없다.
# value : 모든 값을 가질 수 있다.

# 1. 딕셔너리 구조를 직접 만듦
lunch = {'중국집' : '02-971-2312'}
print(lunch)
# 2. dict()함수 이용
dinner = dict(한식='042-999-9999')
print(dinner)
# 3. 중괄호로 초기화 하며 딕셔너리 구조 만듦
bf = {}
bf['분식'] = '012-1231-2132'
print(bf)

menu = {'bf': bf, 'lunch': lunch, 'dinner': dinner}
print(menu)

# 딕셔너리 속 딕셔너리의 값을 받아올때
print(menu['bf']['분식']) 

# 반복문 돌리기
ssafy = {'김은정': '학생', '김인성': '학생', '연용흠': '반장'}
for key in ssafy:
    print(key) # 이렇게 하면 이름이 튀어나와. key를 통해 value에 접근 가능 하므로 key값을 던져줌
    print(ssafy[key]) # 이거는 value가 나와
# 같이 나와
for key, value in ssafy.items():
    print(key, value) 
# print(ssafy.items()) # key와 value를 가지는 튜플들

# value 값만 나와
for vlaue in ssafy.values():
    print(value) 
# key 값만 나옴 (기본 for문 돌려도 동일 결과 나옴)
for key in ssafy.keys():
    print(key)