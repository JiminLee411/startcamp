import requests
from bs4 import BeautifulSoup

# 1. url 설정
url = 'https://finance.naver.com/marketindex/exchangeList.nhn'
# 2. 요청 보내기
response = requests.get(url).text
# 3. HTML 문서로 바꾸기
soup = BeautifulSoup(response, 'html.parser')
# 4. 원하는 내용 선택자로 뽑아내기

# 전체 환율 출력
# table = soup.select('body > div > table > tbody > tr')

# for tr in table:
#     print(tr.select('td.sale')[0].text) # select는 list로 반환하기 때문에 몇번째를 안고르면 에러발생

#dollar 및 유로 출력

dollar_rate = soup.select_one('body > div > table > tbody > tr:nth-child(1) > td.sale').text
dollar_name = soup.select_one('body > div > table > tbody > tr:nth-child(1) > td.tit > a').text

print(dollar_name,':',dollar_rate)