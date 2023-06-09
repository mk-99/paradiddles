import random

from telebot import TeleBot, types
from settings import settings

PDLEN = 4

class Paradiddle:
    def __init__(self, hands: int, feet: int, length: int = 4):
        mask = 2 ** (PDLEN * length) - 1
        self.hands = hands & mask
        self.feet = feet & mask
        self.length = length

    def gethands(self) -> int:
        return self.hands

    def getfeet(self) -> int:
        return self.feet

    def hands_as_string(self) -> str:
        s = ""
        for i in range(0, self.length * PDLEN):
            s = s + ('r' if (self.hands >> i) & 1 else 'l')
            if ((i + 1) % PDLEN == 0) and (i < self.length * PDLEN - 1):
                s = s + " "
        return s

    def feet_as_string(self) -> str:
        s = ""
        for i in range(0, self.length * PDLEN):
            s = s + ('R' if (self.feet >> i) & 1 else 'L')
            if ((i + 1) % PDLEN == 0) and (i < self.length * PDLEN - 1):
                s = s + " "
        return s

def make_paradiddles(num: int = 10) -> str:
    list_of_paradiddles = []
    s = ""

    random.seed()

    for i in range(0, num):
        list_of_paradiddles.append(Paradiddle(random.randint(0, 1000000), random.randint(0, 1000000)))

    for prd in list_of_paradiddles:
        s = s + prd.hands_as_string()
        s = s + '\n'
        s = s + prd.feet_as_string()
        s = s + '\n\n'

    return f"<pre>{s}</pre>"

bot = TeleBot(settings.bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("/start")
    markup.add(btn1)

    msg = make_paradiddles()
    bot.send_message(message.from_user.id, msg, parse_mode="HTML", reply_markup=markup)


bot.polling(none_stop=True, interval=0)
