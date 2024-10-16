import random
import time
from datetime import datetime
from app import db, app, socketio
from app.models import SensorData

# Флаг для остановки потока
stop_thread = False

# Функция для эмуляции данных с 50 параметрами
def read_from_serial():
    global stop_thread
    try:
        while not stop_thread:  # Основная проверка флага остановки
            # Эмулируем 50 параметров
            simulated_data = {f"param{i}": round(random.uniform(20.0, 100.0),6) for i in range(1, 51)}
            print(f"Эмулированные данные: {simulated_data}")

            # Сохраняем эмулированные данные в базу
            with app.app_context():
                save_to_db(simulated_data)

            # Отправляем данные через WebSocket
            socketio.emit('new_data', simulated_data)

            # Разделяем задержку на маленькие интервалы с проверкой флага остановки чтобы при остановке приложения не попасть на заснувший поток
            for _ in range(20):  # В сумме 2 секунды (20 * 0.1)
                if stop_thread:  # Если флаг был установлен, выходим из цикла
                    print("Остановка генерации данных...")
                    return  # Прерываем функцию, завершаем поток
                time.sleep(0.1)

    except Exception as e:
        print(f"Ошибка эмуляции работы с COM-портом: {e}")

# Функция для сохранения данных в базу данных
def save_to_db(data):
    new_data = SensorData(timestamp=datetime.now(), **data)
    db.session.add(new_data)
    db.session.commit()
    print("Данные сохранены в базу данных:", new_data)

# Функция для остановки потока
def stop_serial_thread():
    global stop_thread
    stop_thread = True