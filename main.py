import telebot,time
from secret import bot_token
import dicts


bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, dicts.start_phrase)

@bot.message_handler(commands=["pidor"])
def pidor(message):
    bot.send_message(message.chat.id, dicts.call_phrase)
    time.sleep(2)
    bot.send_message(message.chat.id, dicts.say_it(dicts.wait_phrases))
    time.sleep(3)
    bot.send_message(message.chat.id, dicts.desicion_phrase)
    time.sleep(2)
    bot.send_message(message.chat.id, dicts.say_it(dicts.final_phrases))