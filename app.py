from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    print('a')
    print('b')
    return 'Hello World!@#%^'


if __name__ == '__main__':
    app.run()
