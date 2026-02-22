import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_SECRET_FILE = os.getenv("CLIENT_SECRET_FILE")
CLIENT_TOKEN_PICKLE_FILE = os.getenv("CLIENT_TOKEN_PICKLE_FILE")
DATABASE_URL = os.getenv("DATABASE_URL")
