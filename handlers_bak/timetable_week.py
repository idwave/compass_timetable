from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes
import pandas as pd
#from config import REPLY_DATE

CLASS_NAME, CLASS_LETTER, DATE = range(3)

#markup_date = ReplyKeyboardMarkup(REPLY_DATE, resize_keyboard=True, is_persistent=True)

def week_timetable_to_str(class_name):
    df = pd.read_csv('df.csv')
    df = df.loc[(df['class_name'] == class_name)].reset_index(drop=True)
    result = f"Расписание\n"
    for index, row in df.iterrows():
        result += f"Предмет: {row['subject']}\n"

    return result


async def timetable_week(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Ask the user for info about the selected predefined choice."""
    await update.message.reply_text(
        week_timetable_to_str(context.user_data['class']),
        reply_markup=markup_date,
    )

print(week_timetable_to_str('5а класс'))
