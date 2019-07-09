# 0. requests 패키지를 불러온다.
# pip install requests -> pip를 통해 python에서 requests를 다운 받는다.(한 번만 하면됨)
# requests : 요청을 보내주는 패키지
# pip install bs4 : 문서를 찾기 편하게 바꿔주는 패키지(파싱)
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'

# 1. url로 요청(requests.get)을 보내고, response에 저장한다.(문서를 요청) => string으로 저장
response = requests.get(url).text
# 2. 파이썬이 찾기 편한 형식으로 문서를 변경한다.(KOSPI 등의 data를 찾기 위해) => html문서인거 알려주고 읽게함
soup = BeautifulSoup(response, 'html.parser') #'html.parser' -> html문서라는것을 알려주는 코드

# 연습
# print(soup)
# print(type(response))
# print(type(soup))

# 3. KOSPI 값을 찾는다.
kospi = soup.select_one('#KOSPI_now').text  # .text를 이용하여 필요한 값만 뽑아낸다.

print(kospi)
# print(response.text)
# print(type(response.text))