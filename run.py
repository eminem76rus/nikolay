from operator import index

from app import app, db
from app.serial_reader import read_from_serial  # Импорт функции из другого файла
import threading

# Запуск приложения
if __name__ == '__main__':
    #with app.app_context():
    #    db.create_all()  # Создание таблиц в базе данных впервые
    # Создание потока для эмуляции данных с COM-порта
    serial_thread = threading.Thread(target=read_from_serial)
    serial_thread.start()

    # Запуск веб-сервера Flask
    app.run(debug=True, use_reloader=False)  # use_reloader=False, чтобы не дублировать поток
