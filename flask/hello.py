from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!" 
    

@app.route('/python')
def python():
    return 'python is fun!'

@app.route('/dictionary/<string:word>')
def dictionary(word):
    dicdic={
        'apple': '사과',
        'banana':'바나나',
        'pear':'배',
        'watermelon':'수박'
    }
    result=dicdic.get(word,'나만의 단어장에 없는 단어입니다.') # dicdic[]하면 없을때 에러남
    return f'{word}는(은) {result}'