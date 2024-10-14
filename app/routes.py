from flask import render_template
from app import app
from app.models import SensorData  # Импорт модели SensorData

@app.route('/')
def home():
    # Извлечение всех записей из базы данных отсортированных по времени в обратном порядке
    data = SensorData.query.order_by(SensorData.timestamp.desc()).all()

    return render_template('index.html', data=data)