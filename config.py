import os 

class config(object):
  API_ID = int(os.environ.get("API_ID", 6))
  API_HASH = os.environ.get("API_HASH", "")
  TOKEN = os.environ.get("TOKEN", "")
# NO EDITS 
  PIC = "https://telegra.ph/file/124965f314c03a415f1c4.jpg"
  OWNER_USERNAME = "Alone_loverboy"
  OWNER_ID = 1258905497 
  DB_URI = os.environ.get("DATABASE_URL", None)

# My account configuration
# Don't use mine and create 🙂enemy
