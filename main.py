from typing import Final
from telegram import *
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

TOKEN: Final = '7127271146:AAHV8YM3lEXkqA2UhFIv3JMX-Zt9qLJbSdY'
BOT_USERNAME: Final = '@saved_messages_plus_bot'
CURRENT_NOTE: tuple[int, int, str]
ASK_CATEGORY_MESSAGE_ID = int

# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Send me messages that you want to save. I will help you to organize them into categories')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Send me a message that you want to save. Then add it to a category or create a new category.')

async def filter_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await messages.search

# responses
def handle_response(text: str) -> str:
    return text

# handlers
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    chat_id: int = update.message.chat.id
    message_id: int = update.message.id
    text: str = update.message.text
    global CURRENT_NOTE
    CURRENT_NOTE = (chat_id, message_id, text)

    buttons = [[InlineKeyboardButton('Personal', callback_data='personal')], [InlineKeyboardButton('Study', callback_data='study')]]
    # await context.bot.delete_message(chat_id, message_id)

    global ASK_CATEGORY_MESSAGE_ID
    ask_category = await context.bot.send_message(chat_id=chat_id, reply_markup=InlineKeyboardMarkup(buttons), text='Select category:')
    ASK_CATEGORY_MESSAGE_ID = ask_category.message_id
    #await context.bot.delete_message(chat_id, message_id)

async def queryHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    category = update.callback_query.data
    chat_id, message_id, text = CURRENT_NOTE
    await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    await context.bot.send_message(chat_id=chat_id, text=f'#{category}\n{text}')
    await context.bot.delete_message(chat_id=chat_id, message_id=ASK_CATEGORY_MESSAGE_ID)
    update.callback_query.answer()


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('starting bot...')
    app = Application.builder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('filter', filter_command))

    # messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(CallbackQueryHandler(queryHandler))

    # errors
    app.add_error_handler(error)

    print('polling...')
    app.run_polling(poll_interval=3)