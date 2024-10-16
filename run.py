from app import app, socketio
from app.serial_reader import read_from_serial, stop_serial_thread
import threading
import signal
import sys

# Переменная для хранения потока
thread = None


# Функция для корректного завершения приложения
def signal_handler(sig, frame):
    print("Остановка приложения...")

    # Останавливаем эмуляцию данных
    stop_serial_thread()

    # Ждём завершения потока эмуляции данных с таймаутом
    if thread:
        print("Ожидание завершения потока...")
        thread.join(timeout=5)  # Ждём завершения потока не более 5 секунд

    print("Завершение Flask приложения.")

    print("Приложение остановлено.")
    sys.exit(0)


# Обработка сигнала прерывания (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    #with app.app_context():
    #    db.create_all()  # Создание таблиц в базе данных впервые

    # Запуск эмуляции данных в отдельном потоке
    thread = threading.Thread(target=read_from_serial)
    thread.start()

    # Запуск Flask приложения с поддержкой WebSocket
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
