

################## 파일 작성 및 덮어쓰기, 이어쓰기 ####################
########## option 1. 꼭 f.close명령어를 마지막에 작성해야함

# 파일을 연다. (w : 쓰겠다.)

# w : write (덮어쓰기)
# a : append (이어쓰기)
# f = open('ssafy.txt', 'w')
f = open('ssafy.txt', 'a')


# 글을 작성한다.

# 한줄
# f.write('안녕하세요.')

# 여러줄
for i in range(10):
    f.write(f'안녕하세요. {i}\n')


# 파일을 닫는다.
f.close()


###############



########## option 2. 컨택스트 매니저(context manager) with 구문 -> f.close문 필요X
with open('ssafy_with.txt', 'w') as f:
    # 한줄
    #f.write('안녕? 잘써지나...')

    #여러줄
    for i in range(5):
        # f.writelines('안녕!!!\n')
    
        f.writelines(['은정\n', '인성\n'])
