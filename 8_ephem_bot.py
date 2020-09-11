
"""
Домашнее задание №1
Использование библиотек: ephem
* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.
"""
import logging
import ephem
# import datetime
from datetime import datetime
today = datetime.today()
currentYear = datetime.now().year

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def planet(update, context):
    text="Добавьте название планеты на английском"
    update.message.reply_text(text)


def planet_select(update, context):
    # user_text = update.message.text
    # if user_text =='Mars':
    #   # var=getattr(ephem,user_text)
    #     pl=ephem.Mars(currentYear)
    #     constel=ephem.constellation(pl)
    #     update.message.reply_text(constel)
    try:
        user_text = update.message.text
        var = getattr(ephem, user_text)
        pl = var(currentYear)
        constel = ephem.constellation(pl)
        update.message.reply_text(constel)

    except:
        update.message.reply_text("Такой планеты не существует. Введите другую планету!")




def main():
    mybot = Updater("1397084816:AAFWzpPtbPawQrxl1meF9GkRKZUu0yz2XGU", request_kwargs=PROXY,use_context=True)

    dp = mybot.dispatcher
    # dp.add_handler(CommandHandler("start", greet_user))
    # dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, planet_select))


    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
