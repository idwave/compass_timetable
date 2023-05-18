

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

from handlers.tablereader import get_tomorrow_timetable

from config import REPLY_DATE

CLASS_NAME, CLASS_LETTER, DATE = range(3)

markup_date = ReplyKeyboardMarkup(REPLY_DATE, resize_keyboard=True, is_persistent=True)

LESSON_NUMBER={1: '1️⃣',
                2: '2️⃣',
                3: '3️⃣',
                4: '4️⃣',
                5: '5️⃣',
                6: '6️⃣',
                7: '7️⃣',
                8: '8️⃣',
                9: '9️⃣',
                10: '🔟',
                11: '1️⃣1️⃣',
                }
def tomorrow_timetable_to_str(class_name):
    df = get_tomorrow_timetable(class_name)
    output_string = f"Расписание на завтра:\n\n"
    for index, row in df.iterrows():
        output_string += (
            f"{LESSON_NUMBER[row['number']]} урок с "
            f"{row['time'].split('-')[0]} до {row['time'].split('-')[1]}\n"
            f"       – {str(row['subject']).capitalize()} "
)
        output_string += f"в {row['room']} кабинете\n" if str(row['room']) != 'nan' else "\n"
    return output_string

async def timetable_tomorrow(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Ask the user for info about the selected predefined choice."""
    await update.message.reply_text(
        tomorrow_timetable_to_str(context.user_data['class']),
        reply_markup=markup_date,
    )
