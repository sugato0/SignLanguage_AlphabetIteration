

import mediapipe as mp

import cv2
from modelAlphabet import loaded_model
from ImageProcessing import GetLmListFromImg
# -*- coding: utf-8 -*-
import cv2
import os
import telebot
from telebot import types
import glob
import time



def neuro_guess(pred_arr,message):
  convert_pred = dict()
  print(pred_arr)
  for _ in enumerate(pred_arr[0]):
    convert_pred[_[0]] = _[1]


  asd= sorted(convert_pred.items(), key=lambda item: item[1], reverse=True)
  print(asd)
  y_classes = ["А", "Б", "С", "Ч", "Е", "Ф", "Г", "Х", "И", "Л", "М",
               "Н", "О", "П", "Р", "Ш", "Т", "У", "В", "Я", "Ы",
               "Ю", "Ж"]
  bot.send_message(message.chat.id, "Это буква <<" + str(y_classes[asd[0][0]])+">>\n может быть <<" + str(y_classes[asd[1][0]]) +
                   ">> или <<"+ str(y_classes[asd[2][0]])+">>" )

#from bot father
API_bot = '5625587554:AAHE72ZqDwOecsAEK_EV8ujL7y52kLpOUEk'
bot = telebot.TeleBot(API_bot)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Наша команда")
    btn2 = types.KeyboardButton("Пример жестов")
    markup.add(btn1)
    markup.add(btn2)
    bot.send_message(message.chat.id,
                     text="<--- Привет!Покажи мне буквы правой рукой на жестовом языке"
                          " (напиши пример жестов чтобы просмотреть возможные варианты)--->".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=["text"])
def photo_prediction(message):
    if message.text == "Наша команда":
        bot.send_message(message.chat.id,"Сахаров Данила Сергеевич "
                                         "\n telegramm:@SugatoKavary "
                                         "\n Попова Александра Алексеевна "
                                         "\n telegramm:@zvukii_paniki\n"
                                         " Марьяна Молчанова-Великая Алексеевна"
                                         " \ntelegramm:@kotoylitka "
                                         "\n  https://sugato0.github.io/SignLanguage_numbersIteration_Page/ ")
    if message.text == "Пример жестов":
        bot.send_photo(message.chat.id, photo=("https://drive.google.com/file/d/1W4pQxvJ2cqIy3StZRi1lZfiWD_FRb6KC/view?usp=sharing"))
@bot.message_handler(content_types=["photo"])
def photo_prediction(message):


    # photo downloading

    FilePath = bot.get_file(message.photo[len(message.photo) - 1].file_id).file_path
    downloaded_file = bot.download_file(FilePath)

    src = 'DataImages/' + message.photo[1].file_id
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)





    try:
        #function from libriry
        #getting list [x,y]
        data_our_image = GetLmListFromImg(src)

        print(data_our_image)
        #predict and get list with result
        prediction = loaded_model.predict(data_our_image)
        #func for outputing
        neuro_guess(prediction,message)
    except Exception as e:

        bot.send_message(message.chat.id, "С этим изображением что-то не так")
        print(e)
    for file in glob.glob("DataImages/*")[0:1]:
        os.remove(file)


if __name__ == '__main__': # чтобы код выполнялся только при запуске в виде сценария, а не при импорте модуля
    try:
       bot.polling(none_stop=True) # запуск бота
    except Exception as e:
       print(e) # или import traceback; traceback.print_exc() для печати полной инфы
       time.sleep(15)










