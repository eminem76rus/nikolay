from app import db

# Модель данных для хранения 50 параметров
class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)

    # Добавим 50 параметров
    param1 = db.Column(db.Float, nullable=False)
    param2 = db.Column(db.Float, nullable=False)
    param3 = db.Column(db.Float, nullable=False)
    param4 = db.Column(db.Float, nullable=False)
    param5 = db.Column(db.Float, nullable=False)
    param6 = db.Column(db.Float, nullable=False)
    param7 = db.Column(db.Float, nullable=False)
    param8 = db.Column(db.Float, nullable=False)
    param9 = db.Column(db.Float, nullable=False)
    param10 = db.Column(db.Float, nullable=False)
    param11 = db.Column(db.Float, nullable=False)
    param12 = db.Column(db.Float, nullable=False)
    param13 = db.Column(db.Float, nullable=False)
    param14 = db.Column(db.Float, nullable=False)
    param15 = db.Column(db.Float, nullable=False)
    param16 = db.Column(db.Float, nullable=False)
    param17 = db.Column(db.Float, nullable=False)
    param18 = db.Column(db.Float, nullable=False)
    param19 = db.Column(db.Float, nullable=False)
    param20 = db.Column(db.Float, nullable=False)
    param21 = db.Column(db.Float, nullable=False)
    param22 = db.Column(db.Float, nullable=False)
    param23 = db.Column(db.Float, nullable=False)
    param24 = db.Column(db.Float, nullable=False)
    param25 = db.Column(db.Float, nullable=False)
    param26 = db.Column(db.Float, nullable=False)
    param27 = db.Column(db.Float, nullable=False)
    param28 = db.Column(db.Float, nullable=False)
    param29 = db.Column(db.Float, nullable=False)
    param30 = db.Column(db.Float, nullable=False)
    param31 = db.Column(db.Float, nullable=False)
    param32 = db.Column(db.Float, nullable=False)
    param33 = db.Column(db.Float, nullable=False)
    param34 = db.Column(db.Float, nullable=False)
    param35 = db.Column(db.Float, nullable=False)
    param36 = db.Column(db.Float, nullable=False)
    param37 = db.Column(db.Float, nullable=False)
    param38 = db.Column(db.Float, nullable=False)
    param39 = db.Column(db.Float, nullable=False)
    param40 = db.Column(db.Float, nullable=False)
    param41 = db.Column(db.Float, nullable=False)
    param42 = db.Column(db.Float, nullable=False)
    param43 = db.Column(db.Float, nullable=False)
    param44 = db.Column(db.Float, nullable=False)
    param45 = db.Column(db.Float, nullable=False)
    param46 = db.Column(db.Float, nullable=False)
    param47 = db.Column(db.Float, nullable=False)
    param48 = db.Column(db.Float, nullable=False)
    param49 = db.Column(db.Float, nullable=False)
    param50 = db.Column(db.Float, nullable=False)
