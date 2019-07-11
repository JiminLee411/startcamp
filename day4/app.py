import random
# 0. flask 패키지 가져오기
from flask import Flask, render_template, request

# 1. app 설정
app = Flask(__name__)

# 2. 요청 경로(route) + 함수 만들기
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<string:name>')
def hello(name):
    return render_template('hello.html', name = name)

@app.route('/lunch')
def lunch():
    menus = ['네드코코넛누들', '소불고기', '삼계탕', '싸이버거', '치킨']
    pick = random.choice(menus)
    return render_template('lunch.html', menus = menus, pick=pick)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    # 사용자가 보낸 데이터를 받아와서
    text = request.args.get('say')
    nn = request.args.get('nn')
    print(request.args)
    # 템플릿에 넘겨준다.
    return render_template('pong.html', text=text, nn=nn)

@app.route('/random')
def randompast():
    return render_template('random.html')

@app.route('/random/result')
def result():
    name = request.args.get('name')
    gender = request.args.get('gender')
    past = ['호랑이', '토끼', '사람', '개미', '이구아나', '꽃', '사슴', '기린', '코끼리', '새']
    pick2 = random.choice(past)



    return render_template('result.html',pick2=pick2, name=name, gender=gender)

if __name__ == '__main__':
    app.run(debug=True)