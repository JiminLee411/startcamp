
# window - 한글 잡는것 cp949 (encoding)
# mac/web... - utf-8
# r : read
with open('ssafy_with.txt','r') as f:
    # #있는 그대로 배열
    # print(f.read())
    # #한줄로 배열
    # print(f.readlines())

    # readlines : 모든 라인을 각각 리스트의 원소로 가져와 반환한다. -> 반복문을 돌려야 전체 내용을 볼 수 있다.
    lines = f.readlines()

for line in lines:
    # print(line) # 개행문자로 2줄씩 띄어짐
    print(line.strip()) # strip() : 앞뒤의 공백을 없애준다.


with open('ssafy.txt', 'r') as f:
    # read : 전체 내용을 하나의 string으로 반환한다. -> 바로 전체 내용을 확인 가능하다.
    txt = f.read()

print(txt)
print(type(txt))