import telebot
students = []
students_name = []
teachers = []
teachers_name = []
token = "5450756390:AAHTv5BpWvZHO7ZaEFoHCblHtJ07r2PIOFk"
bot = telebot.TeleBot(token=token)
@bot.message_handler(commands=['start'])
def echo(message):
    user = message.chat.id
    if (user in teachers):
        bot.send_message(user, "начнем? /functions")
    if (user in students):
        bot.send_message(user, "оповещений пока нет")
    else:
        bot.send_message(user, "Добро пожаловать в систему оценок PolyHack_mark бота!")
        bot.send_message(user, "укажите кто вы")
        ans = bot.send_message(user, "я ученик: /student\nя учитель: /teacher")
        bot.register_next_step_handler(ans, chouse)
def chouse(message):
    user = message.chat.id
    text = message.text
    if (text == "/student"):
        ans = bot.send_message(user, "Введите свою фамилию и имя")
        bot.register_next_step_handler(ans, student_name1)
    if (text == "/teacher"):
        ans = bot.send_message(user, "Введите пин код для регистрации")
        bot.register_next_step_handler(ans, teacher_pass)
def student_name1(message):
    user = message.chat.id
    text = message.text
    students.append(user)
    students_name.append(text)
    if (user in students and text in students_name):
        bot.send_message(user, "Готово!")
        for i in range(len(students)):
            print(students[i], students_name[i])
def teacher_pass(message):
    user = message.chat.id
    text = message.text
    if (text == "1357"):
        bot.send_message(user, "Успешно!")
        ans = bot.send_message(user, "введите свое имя и фамилию")
        bot.register_next_step_handler(ans, teacher_name1)
    elif (text != "1357"):
        bot.send_message(user, "Пароль набран не правильно")
def teacher_name1(message):
    user = message.chat.id
    text = message.text
    teachers.append(user)
    teachers_name.append(text)
    if (user in teachers and text in teachers_name):
        bot.send_message(user, "Готово!")
        for i in range(len(teachers)):
            print(teachers[i], teachers_name[i],"teacher")
        bot.send_message(user, "посмотреть функции: /functions")
@bot.message_handler(commands=['functions'])
def office(message):
    user = message.chat.id
    if (user in teachers):
        ans = bot.send_message(user, "отправить опрос о том как прошел урок: /question")
        bot.register_next_step_handler(ans, functions1)
    else:
        pass
def functions1(message):
    user = message.chat.id
    text = message.text
    if (text == "/question"):
        for i in range(len(students)):
            bot.send_message(students[i], "Небольшой опрос от учителя!")
            bot.send_message(students[i], "Как вы оцениваете свое понимание на уроке?")
            bot.send_message(students[i], "я понял тему урока: /true")
            ans = bot.send_message(students[i], "я непонял тему урока: /false")
            bot.register_next_step_handler(ans, mark)
def mark(message):
    user = message.chat.id
    text = message.text
    if (text == "/true"):
        bot.send_message(user, "спасибо за оценку!")
    if (text == "/false"):
        ans = bot.send_message(user, "напишите, что вам не понятно")
        bot.register_next_step_handler(ans, description)
def description(message):
    user = message.chat.id
    text = message.text
    a = students.index(user)
    for w in range(len(teachers)):
        bot.send_message(teachers[w], "Ученику(це) под именем:")
        bot.send_message(teachers[w], students_name[a])
        bot.send_message(teachers[w], "не понятен последний урок, коментарий:")
        bot.send_message(teachers[w], text)
bot.polling(none_stop=True)