import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # 루트 디렉토리에 들어오면 def를 실행하라.
def hello():
    return render_template('hello.html') # hello.html을 렌더링하라는 명령어


@app.route('/hi')
def hi():
    return render_template('hi.html')

# variable routing! 경로를 변수로 활용한다.
# string:name에서 받은 인자를 넘겨준다.
@app.route('/hi/<string:name>')
def hiso(name):
    return render_template('hi2.html', namee=name)

# /cube/<숫자>
# 세제곱 결과를 보여주는 페이지!

@app.route('/cube/<int:num>')
def cube(num):
    return f'{num**3}!!!'

# /lunch/사람이름
# menu = []
@app.route('/lunch/<string:name>')
def lunch(name):
    total_menu = ['일식', '중식', '한식', '양식']
    sel = random.choice(total_menu)
    return render_template('lunch.html', namee=name, pick=sel)


# /lotto
# 로또 번호 6개를 추천해주는 페이지
@app.route('/lotto')
def lotto():
    lotto_num = random.sample(range(1,46), 6)
    lotto_num = str(lotto_num)

    return f'이번주 당첨번호는 {lotto_num} !!'

## html은 문서만 작성 가능해서 랜덤변수 사용 불가.
## flask는 랜덤으로 이용 가능.

if __name__== '__main__':
    # debug mode : on 으로 변경
    # -> flask run을 계속 명령안해도 됨.
    #  python app.py를 치면 저장만 하면 바로 아래의 코드 블록을 실행시킨다.
    app.run(debug=True)