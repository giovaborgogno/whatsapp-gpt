from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from decouple import config as env

DB_POSTGRES = env('DB_POSTGRES')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    context = Column(Text, default='')

engine = create_engine(DB_POSTGRES)
Session = sessionmaker(bind=engine)

session = Session()

def get_user_context(username):
    user = session.query(User).filter_by(username=username).first()
    if user is None:
        user = User(username=username, context="")
        session.add(user)
        session.commit()
    return user.context

def edit_user_context(username, new_context):
    user = session.query(User).filter_by(username=username).first()
    user.context = new_context
    session.commit()





