import wikipedia
import telebot

wikipedia.set_lang('ru')
bot = telebot.TeleBot('your code')


@bot.message_handler(commands=['start'])
def start(message):
    sending_message = f'<b>Привет {message.from_user.first_name}!</b>\n' \
                      f'Чтобы приступить к поиску Введите нужное слово и получите ответ.'
    bot.send_message(message.chat.id, sending_message, parse_mode='html')


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ''
    word = message.text.strip().lower()
    final_message = wikipedia.summary(word)
    bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)
