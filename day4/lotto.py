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

my_lotto = random.sample(range(1, 46), 6)
my_lotto.sort()

comp = list(set(my_lotto)-set(win_lotto))

val = 6 - len(comp)

if val == 6:
    print('1등')
elif val == 5:
    for num in comp:
        if num == bonus:
            print('2등')
        else:
            print('3등')
elif val == 4:
    print('4등')
elif val == 3:
    print('3등')
else:
    print('다음기회에')
