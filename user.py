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


BASE = declarative_base()
SESSION = start()




def get_user_id(message_id: int):
    """ get the user_id from the message_id """
    try:
        s__ = SESSION.query(Users).get(str(message_id))
        return int(s__.chat_id), s__.um_id
    finally:
        SESSION.close()

