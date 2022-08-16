import requests

#Talk to @BotFather(https://t.me/BotFather). Send /newbot to them and follow the prompts. In response you will get an HTTP API token 
#(it will look something like 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11).

#Talk to your newly created bot, it is enough to just /start it.

#Immediately open https://api.telegram.org/bot<token>/getUpdates?offset=-1 in your web-browser 
#(literally paste the token you received from the BotFather, complete with all the letters and punctuation). 
#Copy the chat id from the returned JSON object.

def telegram_bot_sendtext(bot_message):

   BOT_TOKEN = '<your bot token>'
   BOT_CHAT_ID = '<YOUR_BOT_CHAT_ID>'
   SEND_TEXT = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + BOT_CHAT_ID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(SEND_TEXT)
   return response.json()
  
test = telegram_bot_sendtext("Testing Telegram bot")
print(test)