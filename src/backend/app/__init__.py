from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
Bootstrap(app)
app.config.from_object('config.DevelopmentConfig')

from app import views

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

db.create_all()