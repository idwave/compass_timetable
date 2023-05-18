

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

from handlers.tablereader import get_current_lesson

from config import REPLY_DATE

CLASS_NAME, CLASS_LETTER, DATE = range(3)

markup_date = ReplyKeyboardMarkup(
        REPLY_DATE,
        resize_keyboard=True,
        is_persistent=True,
)

def current_lesson_to_str(class_name):
    df, lesson_index = get_current_lesson(class_name)
    index = lesson_index//2
    if lesson_index == -1:
        output_string = f"Уроки либо закончились, либо еще не начались"
    else:
        if lesson_index % 2 == 0:
            output_string = (
                f"Сейчас идет урок "
                f"{df['subject'][index].capitalize()} в {df['room'][index]} "
                f"кабинете.\nСледующий урок {df['subject'][index+1].capitalize()} "
                f"начнется в {df['time'][index+1].split('-')[0]} в "
                f"{df['room'][index+1]} кабинете."
)
        else:
            output_string = (
                f"Сейчас перемена!\nСледующий урок "
                f"{df['subject'][index+1].capitalize()} начнется в "
                f"{df['time'][index+1].split('-')[0]} в "
                f"{df['room'][index+1]} кабинете."
)
    return output_string

async def timetable_now(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        current_lesson_to_str(context.user_data['class']),
        reply_markup=markup_date,
    )

