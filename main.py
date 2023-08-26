from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import Update

TOKEN = '6233009545:AAGF-pxxq0B7BhOUILkmOeuM28OgoyWi67o'

updater = Updater(token=TOKEN)


dp = updater.dispatcher


def start(update: Update, context: CallbackContext):
    name=update.message.chat.first_name
    chat = update.message.chat.id
    context.bot.sendMessage(chat, f'salom {name} xush kelibsiz!')

def echo(update: Update, context: CallbackContext):
    chatid = update.message.chat.id
    text = update.message.text

    context.bot.sendMessage(chatid, text)
def echo_photo(update:Update,context:CallbackContext):
    chatid=update.message.chat.id
    photo=update.message.photo[-1]
    context.bot.sendPhoto(chatid,photo)

def echo_audio(update:Update,context:CallbackContext):
    chatid=update.message.chat.id
    audio=update.message.audio

    context.bot.send_audio(chatid,audio)


dp.add_handler(handler=CommandHandler('start', start))
dp.add_handler(handler=MessageHandler(filters=Filters.text, callback=echo))
dp.add_handler(handler=MessageHandler(filters=Filters.photo, callback=echo_photo))
dp.add_handler(handler=MessageHandler(filters=Filters.audio, callback=echo_audio))

updater.start_polling()
updater.idle()