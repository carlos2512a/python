from tipo import Tipo
import os
from dotenv import load_dotenv


load_dotenv()
host = os.getenv("HOST")
passwd = os.getenv("PASS")
user = os.getenv("USER")
db = os.getenv("DB")
print (host)
