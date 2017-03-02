import telebot
import time
import googl
import urllib
import configparser
from telebot import types

def long_url(text):
    text = urllib.parse.quote_plus(text)
    long_url = 'https://lmgtfy.com/?q='+ text
    return long_url

def short_url(url):
    result = client.shorten(url)
    short_url = result['id']
#    short_url = googl.shortenURL(url)
    return short_url

config = configparser.ConfigParser()
config.sections()
config.read('lmgtfy_bot.conf')

bot = telebot.TeleBot(config['DEFAULTS']['bot_token'])
client = googl.Googl(config['DEFAULTS']['google_client'])

# @bot.inline_handler(func=lambda m: True)
# def query_text(inline_query):
#     try:
#         if inline_query.from_user.username:
#             print(inline_query.from_user.username + ' ' + inline_query.query)
#         else:
#             print(str(inline_query.from_user.id) + ' ' + inline_query.query)
#         l_url = types.InlineQueryResultArticle('long_url', 'Long url', long_url(inline_query.query), disable_web_page_preview=True, description=inline_query.query)
#         s_url = types.InlineQueryResultArticle('short_url', 'Short url', short_url(long_url(inline_query.query)), disable_web_page_preview=True, description=inline_query.query)
#         if len(inline_query.query) > 3:
#             bot.answer_inline_query(inline_query.id, [l_url, s_url])
#             time.sleep(2)
#     except Exception:
#         print('Erro: ' + inline_query.query)
#         pass

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome!\nText me what you want to search\n\nRate the bot:\n'
        'https://telegram.me/storebot?start=lmgtfy_bot')

@bot.message_handler(commands=['info'])
def send_welcome(message):
    info = ('This bot is under constant development!\n'
        'If you have any question or suggestion,\n'
        'please, talk to me!\nTwitter: GabRF\n'
        'Telegram: @GabrielRF\n'
        'Website: http://gabrf.com\n'
        '\nRate the bot:\nhttps://telegram.me/storebot?start=lmgtfy_bot'
        '\nSupport the project:\nhttp://grf.xyz/paypal'
        '\n\nSource-code:'
        '\nhttps://github.com/GabrielRF/telegram-lmgtfy_bot')
    bot.reply_to(message, info)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    #print(message.text)
#    long_url = 'a'
    url = long_url(message.text)
    #print(url)
    bot.reply_to(message, 'Long url:\n'+ url + '\nShort url:\n' + short_url(url), disable_web_page_preview=True)

try: 
    bot.polling(none_stop=True)
except urllib.error.HTTPError:
    time.sleep(10)


while True:
    time.sleep(20)
