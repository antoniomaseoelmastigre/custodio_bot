from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, CommandHandler, Filters
import os


#Functions
def newuser(update: Update, context: CallbackContext):
    update.message.reply_text(f"Bienvenido al grupo @{update.message.new_chat_members[0].username}, ¿ya sabes algo de "
                              f"Python?")
    print(f"Se unió el usuario  @{update.message.new_chat_members[0].username}")


#Start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hola.")
    print("Un usuario inició el bot.")


def main():
    token = os.environ["TOKEN"]

    bot = telegram.bot(token=token)

    updater = Updater(token, use_context=True)

    dispatcher = updater.dispatcher

    #Handlers
    dispatcher.add_handler(CommandHandler("start", callback=start))
    dispatcher.add_handler(MessageHandler(filters=Filters.status_update.new_chat_members, callback=newuser))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
