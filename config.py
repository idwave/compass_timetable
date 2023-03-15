import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
SHEET_ID = '1dI7k4iL_luKdeh9ufMsw8waSsiNI5BYVwvTYaixVlIU'
SHEET_NAME = '1165338981'
REPLY_DATE = [
    ["Сейчас", "Сегодня"],
    ["Завтра", "Неделя"],
    ["Выбрать другой класс"],
]
BASE_DIR = Path(__file__).resolve().parent

