# init SQL 
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (
    Column,
    String,
    Integer 
  )
  # config 
from config import config

# Sql 

def start() -> scoped_session:
    engine = create_engine(config.DB_URI)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))
    
try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    # this is a dirty way for the work-around required for #23
    print("DB_URI is not configured. Features depending on the database might have issues.")
    print(str(e))
 
 # for outgoing of message



def get_user_id(message_id: int):
    """ get the user_id from the message_id """
    try:
        s__ = SESSION.query(Users).get(str(message_id))
        return int(s__.chat_id), s__.um_id
    finally:
        SESSION.close()

