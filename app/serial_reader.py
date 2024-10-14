#import serial
#from datetime import datetime
import random
import time
from datetime import datetime
from app import db, app
from app.models import SensorData

# Функция для чтения данных с COM-порта
#def read_from_serial():
#    try:
#        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Настройка порта и скорости
#        while True:
#            if ser.in_waiting > 0:
#                data = ser.readline().decode('utf-8').strip()
#                if data:
#                    save_to_db(float(data))  # Сохранение в БД
#    except serial.SerialException as e:
#        print(f"Ошибка работы с COM-портом: {e}")

# Функция для эмуляции данных с COM-порта
def read_from_serial():
    try:
        while True:
            # Эмулируем получение данных через случайные значения
            simulated_data = random.uniform(20.0, 100.0)  # Эмулированные данные
            print(f"Эмулированные данные: {simulated_data}")

            # Сохраняем эмулированные данные в базу
            with app.app_context():
                save_to_db(simulated_data)

            # Эмулируем задержку, как будто данные поступают с COM-порта
            time.sleep(2)  # Ожидание 2 секунды между передачами данных
    except Exception as e:
        print(f"Ошибка эмуляции работы с COM-портом: {e}")

# Функция для сохранения данных в базу данных
def save_to_db(value):
    new_data = SensorData(timestamp=datetime.now(), value=value)
    db.session.add(new_data)
    db.session.commit()
