from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json, os

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # db.create_all()


'''
Person
Have title and release year
'''
class Person(db.Model):  
  __tablename__ = 'People'

  id = Column(db.Integer, primary_key=True)
  name = Column(db.String(128))
  city = Column(db.String(128))
  catchphrase = Column(db.String(128))

  def __init__(self, name, city="Concord", catchphrase=""):
    self.name = name
    self.city = city
    self.catchphrase = catchphrase

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'city': self.city,
      'catchphrase': self.catchphrase}