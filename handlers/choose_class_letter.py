#!/usr/bin/env python3


from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

from services.create_timetable import dic_of_classes_with_labels
from config import SHEET_ID, SHEET_NAME 

reply_letter = dic_of_classes_with_labels(SHEET_ID,SHEET_NAME)

CLASS_NAME, CLASS_LETTER = range(2)

async def choose_class_letter(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = update.message.text
    context.user_data["class_number"] = text
    #if context.user_data["class_number"] == '2':
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

