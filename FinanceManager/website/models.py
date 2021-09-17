from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# o sa fac astfel incat fiecare row (spre exemply "spent so far")
# sa se afle in legatura directa cu User-ul
# ca la blog post insa punem row aici


class Row(db.Model):  # each row of the spendings table (such as "Spent so far")
    id = db.Column(db.Integer, primary_key=True)

    # coloana din stanga cu numele gen "my budget"
    text_data = db.Column(db.String(50))
    # coloana din dreapta cu suma alocata pentru 'x' (gen "1500" + "currency type")
    finance_data = db.Column(db.Integer)

    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # for each row we can now reference who created it
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    rows = db.relationship('Row')  # from user reference all rows by their id
