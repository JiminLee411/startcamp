import os


# 1. dummy 폴더로 들어간다.
os. chdir('./dummy')
print(os.getcwd())

# 2. 하나하나씩 파일명을 변경한다. -> 반복문
files = os.listdir('.')

# 현재 명에서 더하는것
# for file in files:
#     os.rename(file, f'SAMSUNG_{file}')

# 현재있는 단어를 다른것으로 변경
for file in files:
    os.rename(file, file.replace('SAMSUNG', 'SSAFY'))



# 문자열에서 조작
# fruit = 'apple, bananan'
# print(fruit.replace('a', ''))