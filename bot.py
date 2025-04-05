import telebot

bot = telebot.TeleBot("7787977250:AAEsD1NrJCDIzubCa9yG0ua3TKxUeUjlGwE")

komand = "/helpeko - как помочь экологии в общем не смотря на возраст"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"привет! это бот для экологии, вот все мои команды {komand}, а для начала скажи мне, ты подросток(10-19, напиши /teenager ) или более взрослый(старше 20ти, напиши /adult )")

@bot.message_handler(commands=['teenager'])
def send_welcome(message):
    bot.reply_to(message, "подростки деляться на более рание и более поздние, сначала я перечислю факты которые может сделать более раниий подросток(10-14), а после более подзний(15-19):")
    with open('C:\\Users\\Svetlana\\m1l1\\eko\\eko.txt', 'r', encoding='utf-8') as f:
        bot.reply_to(message, f.read())
    bot.reply_to(message, "а теперь для более поздних подростков:")
    with open('C:\\Users\\Svetlana\\m1l1\\eko\\eko2.txt', 'r', encoding='utf-8') as f:
        bot.reply_to(message, f.read())
                 
@bot.message_handler(commands=['adult'])
def send_welcome(message):
    bot.reply_to(message, "взрослые могут больше чем подростки, поэтому вот и список для взрослых:")
    with open('C:\\Users\\Svetlana\\m1l1\\eko\\eko3.txt', 'r', encoding='utf-8') as f:
        bot.reply_to(message, f.read())

bot.message_handler(commands=['helpeko'])
def send_welcome(message):
    bot.reply_to(message, "вот вам топ способом помочь экологии:")
    with open('C:\\Users\\Svetlana\\m1l1\\eko\\eko4.txt', 'r', encoding='utf-8') as f:
        bot.reply_to(message, f.read())

bot.infinity_polling()
