import os
from dotenv import load_dotenv
load_dotenv()

APP_USERNAME = os.getenv("APP_USERNAME", None)
APP_PASSWORD = os.getenv("APP_PASSWORD", None)