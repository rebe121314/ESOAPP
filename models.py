from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Scholarship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    amount = db.Column(db.String(50))
    currency = db.Column(db.String(10))
    deadline = db.Column(db.String(50))
    apply_link = db.Column(db.String(500))
    citizenships = db.Column(db.String(200))
    eligibility_criteria = db.Column(db.Text)
    application_process = db.Column(db.Text)
    awarding_institution = db.Column(db.String(120))
    general_information = db.Column(db.Text)
    tag = db.Column(db.String(120))
    keywords = db.Column(db.String(200))
