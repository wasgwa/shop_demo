
# coding=utf-8

token = '570072830:AAE2HjqGmDlw_MyKmA5EVxNhAI0MpUJyoL0'
import telebot
import requests

bot = telebot.TeleBot(token)


def get_btc_usd():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    a = requests.get(url)
    r = a.json()
    price = r['ticker']['last']
    return price


def get_btc_usd_crypta():
    url = 'https://api.cryptonator.com/api/full/btc-usd'
    a = requests.get(url)
    r = a.json()
    price = r['ticker']['price']
    return price


def get_btc_rub():
    url = 'https://yobit.net/api/2/btc_rub/ticker'
    a = requests.get(url)
    r = a.json()
    price = r['ticker']['last']
    return price


def get_eth_usd():
    url = 'https://yobit.net/api/2/eth_usd/ticker'
    a = requests.get(url)
    r = a.json()
    price = r['ticker']['last']
    return price


def fixAns(m):
    if (m.text == '/btc'):
        bot.send_message(
            m.chat.id, '1 биткоин = ' + str(get_btc_usd()) + ' usd')
    if (m.text == '/eth'):
        bot.send_message(
            m.chat.id, '1 эфириум = ' + str(get_eth_usd()) + ' usd')
    bot.register_next_step_handler(m, fixAns)


@bot.message_handler(commands=["start"])
def start(m):
    msgtosend = 'Бот курса криптовалют : \r\n'
    msgtosend += '  /btc -информация о курсе биткоина\r\n'
    msgtosend += '  /eth -информация о курсе эфириума\r\n'

    msg = bot.send_message(m.chat.id, msgtosend)
    bot.register_next_step_handler(msg, fixAns)


if __name__ == '__main__':

    bot.polling(none_stop=True)
