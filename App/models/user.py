from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    phoneNumber= db.Column(db.Integer,nullable=True,unique=True)
    email=db.Column(db.String,nullable=False,unique=True)
    password = db.Column(db.String(120), nullable=False)
    workoutLevel= db.Column(db.String(120), nullable=True)

    def __init__(self, username, password,phoneNumber,email,workoutLevel):
        self.username = username
        self.set_password(password)
        self.phoneNumber=phoneNumber
        self.email=email
        self.workoutLevel

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def editUserName(self, userID,username):
        user=User.query.get(userID)
        user.username=username
        user.phoneNumber=data["phoneNumber"]
        user.email=data["email"]
        return message="Edit Successful"
        
    def editphoneNumber(self, userID,phoneNumber):
        user=User.query.get(userID)
        user.username=username
        user.phoneNumber=phoneNumber
        user.email=data["email"]
        return message="Edit Successful"

    def editEmail(self, userID,email):
        user=User.query.get(userID)
        user.email=email
        return message="Edit Successful"


    def deleteAccount(self,userID):
        data=request.json()
        User del_user=User.query.filter_by(userID=data["userID"])
        db.session.delete(del_user)
        db.session.commit()
      return True
    return None

    def signUP(self, username, password,phoneNumber,email,workoutLevel):
        user=User(username,password,phoneNumber,email,workoutLevel)
        db.session.add(user)
        db.session.commit()
        return message="Successfully Added", 201

class Excercise(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, nullable=False, unique=True)
    muscle=  db.Column(db.String, nullable=False)
    workoutLevel =  db.Column(db.String, nullable=False,)
    def __init__(self):
        self.muscle = "TestMuscle"
        self.name="TestName"
        self.workoutLevel=1
        pass

class Routine(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    userID =  db.Column(db.Integer, nullable=False, unique=True)
    excID=  db.Column(db.Integer, nullable=False,unique=True)
    workoutLevel =  db.Column(db.String, nullable=False,)
    pass
