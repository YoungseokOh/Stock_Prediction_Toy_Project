import telegram

bot = telegram.Bot(token='1677916368:AAGEEAK3TomepKeXX6Xw37yh2TaGP6P5lgA')


def get_chat_id(chat_title_name):
    updates = bot.getUpdates()
    for update in updates:
        if update.channel_post and update.channel_post.chat.title == chat_title_name:
            chat_id = update.channel_post.chat.id
            return chat_id


def send_message(chat_id, message):
    bot.sendMessage(chat_id=chat_id, text=message)
