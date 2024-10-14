from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Создание экземпляра Flask-приложения
app = Flask(__name__)

# Настройка подключения к базе данных PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flaskuser:password@localhost/sensor_data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация SQLAlchemy
db = SQLAlchemy(app)

from app import routes  # Импортируем маршруты для регистрации
