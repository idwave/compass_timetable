
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import ContextTypes



async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )
