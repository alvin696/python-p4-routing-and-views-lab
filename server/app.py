#!/usr/bin/env python3


from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<text>')
def print_text(text):
    print(text)
    return text

@app.route('/count/<int:num>')
def count(num):
    result = '\n'.join(str(i) for i in range(num))
    return result

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return 'Invalid operation'

if __name__ == '__main__':
    app.run()

