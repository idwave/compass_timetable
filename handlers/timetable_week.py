from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

from config import REPLY_DATE

CLASS_NAME, CLASS_LETTER, DATE = range(3)

markup_date = ReplyKeyboardMarkup(REPLY_DATE, resize_keyboard=True, is_persistent=True)

def week_timetable_to_str(class_name):
    pass


async def timetable_week(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Ask the user for info about the selected predefined choice."""
    await update.message.reply_text(
        week_timetable_to_str(context.user_data['class']),
        reply_markup=markup_date,
    )

