import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

# Вставьте здесь свой токен, который вы получили от BotFather
TOKEN = ""
bot = telebot.TeleBot(TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=["start"])
def send_welcome(message):
    # Сообщение с описанием
    description_text = "Glad to see you!\n\nFlappy Tokken - arcade game with simple mechanic!\n\nNow we getting better and offer you to try our creation \n\nMade by Nice Guys"

    # Создание кнопки с ссылкой на веб-приложение
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("Play (MOBILE)", url="t.me/ivtmail_bot/flappytoken")
    )
    keyboard.add(InlineKeyboardButton("Our community", url="https://t.me/GuysNice"))

    # Отправка сообщения с описанием и кнопкой
    bot.send_message(message.chat.id, description_text, reply_markup=keyboard)


# Запуск бота
if __name__ == "__main__":
    print("Запуск")
    bot.polling()
