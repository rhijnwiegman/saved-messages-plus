from typing import Final
from telegram import *
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '7127271146:AAHV8YM3lEXkqA2UhFIv3JMX-Zt9qLJbSdY'
BOT_USERNAME: Final = '@saved_messages_plus_bot'

# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Send me messages that you want to save. I will help you to organize them into categories')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Send me a message that you want to save. Then add it to a category or create a new category.')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('')

# responses

def handle_response(text: str) -> str:
    return text

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    buttons = [[InlineKeyboardButton('Personal', callback_data='personal'), InlineKeyboardButton('Urls', callback_data='urls'), InlineKeyboardButton('Personal', callback_data='personal'),InlineKeyboardButton('Personal', callback_data='personal'), InlineKeyboardButton('Personal', callback_data='personal'), InlineKeyboardButton('Personal', callback_data='personal'), InlineKeyboardButton('Personal', callback_data='personal') ], [InlineKeyboardButton('Study', callback_data='study')]]
    response: str = handle_response(text)

    # debug
    print('Bot:', response)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text=response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('starting bot...')
    app = Application.builder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # errors
    app.add_error_handler(error)

    print('polling...')
    app.run_polling(poll_interval=3)