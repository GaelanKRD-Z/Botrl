import requests
import telepot
from telepot.loop import MessageLoop

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
TELEGRAM_BOT_TOKEN = '7225151310:AAFAkqQxQUBfn7SweDysNOypNh7RqsTo8bk'
TRANSLATE_API_URL = 'https://api.mymemory.translated.net/get'

def translate_text(text):
    params = {
        'q': text,
        'langpair': 'en|ckb'
    }
    response = requests.get(TRANSLATE_API_URL, params=params)
    if response.status_code == 200:
        translation = response.json()['responseData']['translatedText']
        return translation
    else:
        return 'Translation failed.'

def handle_message(msg):
    chat_id = msg['chat']['id']
    text = msg['text']
    translated_text = translate_text(text)
    bot.sendMessage(chat_id, translated_text)

bot = telepot.Bot(TELEGRAM_BOT_TOKEN)
MessageLoop(bot, handle_message).run_as_thread()

print('Bot is listening...')


# Keep the program running
import time
while True:
    time.sleep(10)
