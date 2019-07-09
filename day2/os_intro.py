# 운영체제(컴퓨터)를 조작한다
import os

# listdir : ls
# 현재 디렉토리에 있는 파일 및 폴더들을 보여주는 명령어
ls = os.listdir('.')
print(ls)

# getcwd(get current working directory) : pwd
# 현재 파일이 실행된 디렉토리(작업하고 있느 경로)를 알려주는 명령어
pwd = os.getcwd()
print(pwd)

# chdir( change directory) : cd
# 해당 디렉토리 위치로 이동한다.
os.chdir('./dummy')
pwd = os.getcwd()
print (pwd)

