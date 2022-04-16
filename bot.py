from telegram import Update, Bot
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler
from telegram.utils.request import Request
import logging


token = '5148676833:AAGv1DO8rqIHwarcdna9W6OwH1RNytMMP1c'


# Реализация логирования в отдельный файл: bot.log
logging.basicConfig( format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log' )


# Реагирование бота на команду: /start
def start(update: Update, context: CallbackContext):
    text = 'Pressed: /start'
    logging.info(text)
    update.message.reply_text(text) # Самый простой способ ответить пользователю

def main():
    bot = Updater(token)

    logging.info('Bot is working...')

    dp = bot.dispatcher
    dp.add_handler(CommandHandler('start', start))

    bot.start_polling()
    bot.idle() # <= Означает что бот будет работать до тех пор, пока мы его пренудительно не остановим


main()