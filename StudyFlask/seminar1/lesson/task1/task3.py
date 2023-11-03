from flask import Flask

app = Flask(__name__)

@app.get('/calc/<int:num1>/+/<int:num2>')
def calc_sum(num1, num2):
    summ = num1 + num2
    return f'{num1} + {num2} = {summ}'

@app.get('/')
def hello_world():
    return 'Hello world!'

@app.get('/about/')
def about():
    return 'About us.'

@app.get('/contacts/')
def contacts():
    return 'My contacts.'

if __name__ == "__main__":
    app.run(debug=True) #debug=True - позволяет вносить изменения в код при запущенном сервере.
                        #Также только в этом режиме видны ошибки в шаблонах.

