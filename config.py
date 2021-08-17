import os 

class config(object):
  API_ID = int(os.environ.get("API_ID", 6))
  API_HASH = os.environ.get("API_HASH", "")
  TOKEN = os.environ.get("TOKEN", "")
  STRING_SESSION = os.environ.get("STRING_SESSION", "")
# NO EDITS 
  PIC = "https://telegra.ph/file/42aa88442d9266468d11a.jpg"
  OWNER_USERNAME = "Alone_loverboy"
  OWNER_ID = 1258905497 
  DB_URI = os.environ.get("DATABASE_URL", None)

# My account configuration
# Don't use mine and create 🙂enemy
