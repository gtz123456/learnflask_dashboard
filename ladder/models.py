from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from ladder import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))
    privilege = db.Column(db.Integer)
    balance = db.Column(db.Integer)
    referee = db.Column(db.Integer)

    def setPassword(self, password):
        self.password_hash = generate_password_hash(password)
        db.session.commit()

    def validatePassword(self, password):
        return check_password_hash(self.password_hash, password)
    
    def setPrivilege(self, privilege):
        self.privilege = privilege
        db.session.commit()

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
    user.setPassword(password)
    db.session.add(user)
    db.session.commit()







class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份
