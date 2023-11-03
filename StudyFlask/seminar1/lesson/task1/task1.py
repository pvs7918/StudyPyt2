from flask import Flask

app = Flask(__name__)

@app.get('/')
def hello_world():
    return 'Hello world!'


if __name__ == "__main__":
    app.run(debug=True) #debug=True - позволяет вносить изменения в код при запущенном сервере.
                        #Также только в этом режиме видны ошибки в шаблонах.

