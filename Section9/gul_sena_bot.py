import logging
import random

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, ChatMember, ForceReply)
from telegram.ext import (Updater, CommandHandler)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

students = list()
all_students = ['Abdullah', 'Ahmet', 'Ata', 'Ayşe', 'Canan', 'Emirhan', 'Ezgi', 'Furkan',
    'Gamze', 'Gonca', 'Gökçe', 'İlayda', 'Mohsen', 'Seyit', 'Berfin', 'Zeynep', 'Mahsa', 'Gul Sena']

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def hello(update, context):
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    if (not user.first_name in students):
        students.append(user.first_name)
    logger.info("Current students", students)
    # sends message as a reply
    update.message.reply_text(f'Welcome {user.first_name}')

def create_random_person(update, context):
    # pick a random student
    random_person = random.choice(all_students)
    # replace the keyword /who by the random name
    message = update.message.text.replace("/who", random_person)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def echo(update, context):
    """Echo the user message."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Do not change this method
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text=f'Possible commands:\n/echo\n/who\n/start\n/hello\n/who_talked')

def who_talked(update, context):
    students_str = ''
    for s in students:
        students_str += f', {s}'
    context.bot.send_message(chat_id=update.effective_chat.id,
        text=f'Active ones in this session: {students_str}')
        
def main():
    # create an updater object
    # Important!!!
    # Enter your API token here and make sure your file name matches with your bot's name
    updater = Updater(token='', use_context=True)

    # create dispatcher here  
    dispatcher = updater.dispatcher  

    
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    echo_handler = CommandHandler('echo', echo)
    dispatcher.add_handler(echo_handler)

    hello_handler = CommandHandler('hello', hello)
    dispatcher.add_handler(hello_handler)

    dispatcher.add_handler(CommandHandler('who', create_random_person))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('who_talked', who_talked))


    dispatcher.add_error_handler(error)
    
    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

