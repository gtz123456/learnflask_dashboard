from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from ladder import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40))
    password_hash = db.Column(db.String(128))
    privilege = db.Column(db.Integer)
    balance = db.Column(db.Integer)
    referee = db.Column(db.Integer)

    def setPassword(self, password):
        self.password_hash = generate_password_hash(password)

    def validatePassword(self, password):
        return check_password_hash(self.password_hash, password)
    
    def getBalance(self):
        return self.balance

    def setBalance(self, amount):
        self.balance = amount
        db.session.commit()

class GiftCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    amount = db.Column(db.Integer)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ServiceOwner = db.Column(db.Integer)
    ServiceType = db.Column(db.Integer)
    ServiceStartat = db.Column(db.DateTime)
    ServiceEndat = db.Column(db.DateTime)
    ServiceBandwith = db.Column(db.Integer)
    ServiceData = db.Column(db.Integer) # 
    ServiceRenewal = db.Column(db.Integer) # count by day

def generateUser(email, password, privilege, balance=0, referee=0):
    user = User(email=email, privilege=privilege, balance=balance, referee=referee)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()