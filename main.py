import os

# pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env

# env variables

API_KEY = os.getenv("API_KEY")
EMAIL_ADDR = os.getenv("EMAIL_ADDR")
PASSWORD = os.getenv("PASSWORD")

log_info = {
    'api_key': API_KEY,
    'email': EMAIL_ADDR,
    'password': PASSWORD
}

print(log_info)



