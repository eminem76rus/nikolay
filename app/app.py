from operator import index

from flask import Flask, render_template

# Создание экземпляра Flask-приложения
app = Flask(__name__)

# Маршрут для главной страницы
@app.route('/')
def home():
    return render_template('index.html')

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
