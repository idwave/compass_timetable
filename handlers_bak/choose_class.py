from telegram import Update
from telegram.ext import ContextTypes

from telegram import ReplyKeyboardMarkup, Update

CLASS_NAME, CLASS_LETTER = range(2)


reply_class = [
        ["0","1","2","3"],
        ["4","5","6","7"],
        ["8","9","10"],
]

async def choose_class(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Привет, я бот для расписания. Выберите класс",
        reply_markup=ReplyKeyboardMarkup(reply_class, resize_keyboard=True, is_persistent=True),
    )
    return CLASS_NAME


