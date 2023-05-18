#!/usr/bin/env python

import config
import logging
import handlers

from telegram import ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

markup_date = ReplyKeyboardMarkup(config.REPLY_DATE, resize_keyboard=True, is_persistent=True)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

CLASS_NAME, CLASS_LETTER, DATE = range(3)

def main() -> None:
    """Run the bot."""
    application = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", handlers.choose_class)],
        states = {
            CLASS_NAME: [
                MessageHandler(
                    filters.Regex("^(0|1|2|3|4|5|6|7|8|9|10)$"), handlers.choose_class_letter
                )
            ],
            CLASS_LETTER: [
                MessageHandler(
                    filters.Regex("^(а|б|с|р|м|нет подгруппы)$"), handlers.choose_date
                )
            ],
            DATE: [
                MessageHandler(
                    filters.Regex("^Сейчас$"), handlers.timetable_now
                ),
                MessageHandler(
                    filters.Regex("^Сегодня$"), handlers.timetable_today
                ),
                MessageHandler(
                    filters.Regex("^Завтра$"), handlers.timetable_tomorrow
                ),
                MessageHandler(
                    filters.Regex("^Неделя$"), handlers.timetable_week
                ),
                MessageHandler(
                    filters.Regex("^Выбрать другой класс$"), handlers.choose_class
                    ),
            ],
        },
        fallbacks=[CommandHandler("cancel", handlers.cancel)],
    )
    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == "__main__":
    main()
