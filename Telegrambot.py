import telebot
import requests
TOKEN = '5801284115:AAGLI5NND4pfjerTL_uUQvVNswzGcznkbz4'
URL = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcom(message):
    bot.reply_to(message, 'Hi,can i help you?')

@bot.message_handler(func=lambda m: True)
def show_price(message):
    symbol = message.text.upper()
    response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}')
    if response.status_code == 200:
        data = response.json()
        bot.reply_to(message, f'{data["symbol"]} price is {data["price"]}')
    else:
        bot.reply_to(message, 'something is wrong...')


bot.infinity_polling()