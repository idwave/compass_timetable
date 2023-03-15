from telegram import ReplyKeyboardMarkup, Update
from telegram import Update
from telegram.ext import ContextTypes
from config import REPLY_DATE

CLASS_NAME, CLASS_LETTER, DATE = range(3)


markup_date = ReplyKeyboardMarkup(REPLY_DATE, resize_keyboard=True, is_persistent=True)

async def choose_date(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    context.user_data["class_letter"] = text
    if context.user_data["class_number"] == '2':
        context.user_data["class"] = context.user_data["class_number"] + ' класс'
    else:
        context.user_data["class"] = context.user_data["class_number"]\
            + context.user_data["class_letter"]\
            + ' класс'
    await update.message.reply_text(
        f"Ваш класс: {context.user_data['class']}. Показать расписание на:",
        reply_markup=markup_date,
    )

    return DATE

