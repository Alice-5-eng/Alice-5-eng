import telebot

bot = telebot.TeleBot("7959926920:AAE6nwHLRFIsnbpFsFNOB7598hsl62OBvAo")

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Капля", "Киаф","Скифос", "Карас")
    bot.send_message(message.chat.id, "Выберите кнопку:", reply_markup=markup)
    
    
    

@bot.message_handler(func=lambda message: message.text in ["Капля"])
def handle_button(message):
    bot.send_message(message.chat.id, "Введите число:")
    bot.register_next_step_handler(message, process_number)

def process_number(message):
    try:
        number = int(message.text)
        result = number *  4
        bot.send_message(message.chat.id, f"Результат: {result} секунд")
    except ValueError:
        bot.send_message(message.chat.id, "Некорректное значение. Введите число.")



@bot.message_handler(func=lambda message: message.text in ["Киаф"])
def handle_button(message):
    bot.send_message(message.chat.id, "1 Киаф ≈ 14 минут \n Введите число:")
    bot.register_next_step_handler(message, process_number1)

def process_number1(message):
    try:
        number = int(message.text)
        result = number *  14
        bot.send_message(message.chat.id, f"Результат: {result} минут")
    except ValueError:
        bot.send_message(message.chat.id, "Некорректное значение. Введите число.")


@bot.message_handler(func=lambda message: message.text in ["Скифос"])
def handle_button(message):
    bot.send_message(message.chat.id, "1 Скифос ≈ 2 часа и 3 минуты\n Введите число:")
    bot.register_next_step_handler(message, process_number2)

def process_number2(message):
    try:
        number = int(message.text)
        result = number *  2
        rrr = number * 3
        bot.send_message(message.chat.id, f"Результат: {result} часов и {rrr} минут")
    except ValueError:
        bot.send_message(message.chat.id, "Некорректное значение. Введите число.")
        
        
        
@bot.message_handler(func=lambda message: message.text in ["Карас"])
def handle_button(message):
    bot.send_message(message.chat.id, "1 Карас ≈22 часа \n Введите число:")
    bot.register_next_step_handler(message, process_number3)

def process_number3(message):
    try:
        number = int(message.text)
        result = number *  22
        bot.send_message(message.chat.id, f"Результат: {result} часов")
    except ValueError:
        bot.send_message(message.chat.id, "Некорректное значение. Введите число.")

bot.infinity_polling()