from flask import Flask
appl = Flask(__name__)

@appl.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    appl.run()
