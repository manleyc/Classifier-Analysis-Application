from app import db

class Filestorage(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(300))
	data = db.Column(db.LargeBinary)