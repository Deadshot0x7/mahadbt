from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import time as t
import os as s 
from response import *


PORT=int(s.environ.get('PORT','5000'))
TOKEN = '1849563775:AAGGX0GCema6OelGZprpu6AdwjzyoWfeULQ'
updater.bot.setWebhook('https://mahatbtbot.herokuapp.com/' + TOKEN)

t.sleep(2)
print("Bot has been started")
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('bye',b))
updater.dispatcher.add_handler(CommandHandler('chatbot',chat))
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.start_polling()
updater.idle()




