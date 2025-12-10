from extension import db
from datetime import datetime  

class Recommendations(db.Model):
    __tablename__ = "recommendations"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    scan_id = db.Column(db.Integer, db.ForeignKey('posture_scans.id'), nullable=False)
    rekomendasi_makanan = db.Column(db.Text, nullable=False)
    rekomendasi_olahraga = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)