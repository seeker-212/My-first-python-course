from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/page/<int:number>')
def page(number):
    return f'This is page {number}'

if __name__ == '__main__':
    app.run(debug=True)