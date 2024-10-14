from app import db

# Модель данных для хранения данных с датчиков
class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.Float, nullable=False)
