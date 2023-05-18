from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

reply_letter = {
        '1': ['а', 'с', 'р', 'м'],
        '2': ['нет подгруппы'],
        '3': ['а', 'б'],
        '4': ['а', 'б'],
        '5': ['а', 'б'],
        '6': ['а', 'б'],
        '7': ['а', 'б'],
        '8': ['а', 'б'],
        '9': ['а', 'б'],
        '10': ['а', 'б'],
        }

CLASS_NAME, CLASS_LETTER = range(2)

async def choose_class_letter(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = update.message.text
    context.user_data["class_number"] = text
    if len(reply_letter[context.user_data["class_number"]]) == 1:
        await update.message.reply_text(
            f"Вы выбрали {context.user_data['class_number']} класс. Выберете вашу подгруппу",
            reply_markup=ReplyKeyboardMarkup(
                [['нет подгруппы']],
                resize_keyboard=True,
                is_persistent=True),
        )
        return CLASS_LETTER

    await update.message.reply_text(
        f"Вы выбрали {context.user_data['class_number']} класс. Выберете вашу подгруппу",
        reply_markup=ReplyKeyboardMarkup(
            [reply_letter[context.user_data["class_number"]]],
            resize_keyboard=True,
            is_persistent=True),
    )

    return CLASS_LETTER

