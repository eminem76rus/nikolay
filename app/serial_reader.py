import random
import time
from datetime import datetime
from app import db, app
from app.models import SensorData

# Функция для эмуляции данных с 50 параметрами
def read_from_serial():
    try:
        while True:
            # Эмулируем 50 параметров
            simulated_data = {f"param{i}": random.uniform(20.0, 100.0) for i in range(1, 51)}
            print(f"Эмулированные данные: {simulated_data}")

            # Сохраняем эмулированные данные в базу
            with app.app_context():
                save_to_db(simulated_data)

            # Эмулируем задержку
            time.sleep(2)
    except Exception as e:
        print(f"Ошибка эмуляции работы с COM-портом: {e}")

# Функция для сохранения данных в базу данных
def save_to_db(data):
    new_data = SensorData(
        timestamp=datetime.now(),
        **data
    )
    db.session.add(new_data)
    db.session.commit()
    print("Данные сохранены в базу данных:", new_data)

    db.session.add(new_data)
    db.session.commit()
