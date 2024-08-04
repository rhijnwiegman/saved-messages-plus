from typing import Final
from telegram import Update
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
