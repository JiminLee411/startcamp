import random
import pprint
import requests

url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=864"
# 1. 요청
## json -> 파이썬의 dictionary와 list로 변환하여 조작할 수 있다.
## 응답 (HTML, XML, JSON)의 문서를 줄 수 있다.
response = requests.get(url).json() # .json() 붙이면 딕셔너리로 변경해줌
pprint.pprint(response)
print(type(response))

win_lotto = []
bonus = response['bnusNo']

for i in range(1,7):
    win_lotto.append(response[f'drwtNo{i}'])

result = [0, 0, 0, 0, 0]
for i in range(10000000):

    my_lotto = random.sample(range(1, 46), 6)

# 몇개 맞았는지 확인
# matched = 0
# for num in my_lotto:
#     if num in my_lotto:
#         matched += 1

    matched = len(set(win_lotto)& set(my_lotto))

    if matched ==6:
        result[0] +=1
    elif matched == 5 and bonus in my_lotto:
        result[1] +=1
    elif matched == 5:
        result[2] +=1
    elif matched == 4:
        result[3] +=1
    elif matched == 3:
        result[4] +=1

    print(result, end='\r')
print('끝')
print(result)