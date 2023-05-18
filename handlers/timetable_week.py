

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

from handlers.tablereader import get_week_timetable

from config import REPLY_DATE

CLASS_NAME, CLASS_LETTER, DATE = range(3)

markup_date = ReplyKeyboardMarkup(REPLY_DATE, resize_keyboard=True, is_persistent=True)

week_days={'понедельник': '1️⃣',
            'вторник': '2️⃣',
            'среда': '3️⃣',
            'четверг': '4️⃣',
            'пятница': '5️⃣',
}

def week_timetable_to_str(class_name):
    df = get_week_timetable(class_name)
    current_day = 'понедельник'
    output_string = f"Расписание на неделю:\n\n"
    output_string += f"{week_days[current_day]} {current_day.capitalize()}:\n"
    for index, row in df.iterrows():
        if str(row['day']) != current_day:
            current_day = str(row['day'])
            output_string += f"{week_days[current_day]} {current_day.capitalize()}:\n"
        output_string += f"     – {row['number']}. {str(row['subject']).capitalize()}\n"
    return output_string


async def timetable_week(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Ask the user for info about the selected predefined choice."""
    await update.message.reply_text(
        week_timetable_to_str(context.user_data['class']),
        reply_markup=markup_date,
    )

