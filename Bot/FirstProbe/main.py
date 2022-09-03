# import telebot
# from telebot import types
#
# bot = telebot.TeleBot('5515909198:AAGICkdnOTI_JeXEmluVmIz1-WwAPOCaqs0')
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
#     bot.send_message(message.chat.id, mess, parse_mode='html')
#
#
# # @bot.message_handler(content_types=['text'])
# # def get_user_text(message):
# #     if message.text == "Hello":
# #         bot.send_message(message.chat.id, "Hello! Nice to see you.", parse_mode='html')
# #     elif message.text == "id":
# #         bot.send_message(message.chat.id, f"Your ID: {message.from_user.id}", parse_mode='html')
# #     elif message.text == "Photo":
# #         photo = open("photo_2021-11-16_16-36-11.jpg", 'rb')
# #         bot.send_photo(message.chat.id, photo)
# #     else:
# #         bot.send_message(message.chat.id, "I don't understand you.", parse_mode='html')
# #
#
# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id, "Wow! Nice photo.")
#
#
# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Go to Website", url="https://itproger.com"))
#     bot.send_message(message.chat.id, "Move to website.", reply_markup=markup)
#
#
# @bot.message_handler(commands=['help'])
# def website(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     website = types.KeyboardButton('Website')
#     start = types.KeyboardButton('Start')
#
#     markup.add(website, start)
#     bot.send_message(message.chat.id, "Move to website.", reply_markup=markup)
#
#
# bot.polling(none_stop=True)
