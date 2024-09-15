import os
import random
import telebot;
penis = ["https://i.pinimg.com/originals/21/fb/5d/21fb5d9e53ed9d22adcdd6dc98d04bd5.jpg", "https://github.com/MilanFennec/furryfetch/blob/main/0uzffSlGJdhfEtn9DMrOHhc3mx5ShVrQSsu8uDPlM-ZmnHhoZyYPMxxXELIYF-rfg6wY15z0GAaUfI1DzFVDT0W4.jpg?raw=true", "https://github.com/MilanFennec/furryfetch/blob/main/IMG_20240914_190319_475.jpg?raw=true", "https://github.com/MilanFennec/furryfetch/blob/main/IMG_20240907_183453_050.jpg?raw=true"]
xui = ["Я твою мать ебал", "Иди нахуй сын шлюхи", "Ты сосала мне праститутка", "Ты гандон", "http://natribu.org"]
ebat = ["пидр", "мразь", "гандон", "рукоблуд", "давалка"]
bot = telebot.TeleBot("7164076137:AAFR2QVWdYLc8DjpqZW1kgKlUGeX-aVXzlU");
epta = ("сука")
@bot.message_handler(func=lambda message: True, content_types=("text"))
def handle_message(message):
   blyat = ("Ну скожи мне чо нить " + random.choice(ebat) )
   bot.reply_to(message, random.choice(xui))
   bot.send_photo(message.chat.id, photo=(random.choice(penis)))
   bot.reply_to(message, blyat)
bot.polling(none_stop=True, interval=0)
