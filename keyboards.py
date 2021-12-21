from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import random

def decode(emoji, name):
    emoji = emoji.encode("utf-16", "surrogatepass").decode("utf-16", "surrogatepass")
    return str(emoji + ' ' + name)

#КУПИТЬ
bb = InlineKeyboardButton(decode('\ud83d\udc8a', 'Купить'), callback_data='buy')
buy = InlineKeyboardMarkup().row(bb)
bb1 = InlineKeyboardButton('Купить', callback_data='cc')
buy1 = InlineKeyboardMarkup().row(bb1)
bbbb = InlineKeyboardButton(decode('\ud83d\udc8a', 'Купить'), callback_data='buyy')
buyy = InlineKeyboardMarkup().row(bbbb)


#БАЛАНС/ОПЛАТА
bal = InlineKeyboardButton(decode('\u2663\ufe0f', 'Пополнить баланс'), callback_data='bal')
balance = InlineKeyboardMarkup().row(bal)

bal1 = InlineKeyboardButton(decode('\ud83e\udd5d', 'Qiwi'), callback_data='qiwi', url= 'https://www.google.com/search?q=%D0%94%D0%98%D0%9C%D0%90+%D0%9F%D0%98%D0%94%D0%90%D0%A0%D0%90%D0%A1&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi929X-3fX0AhXSk4sKHdh5ClAQ_AUoAXoECAEQAw&biw=1920&bih=969&dpr=1#imgrc=RVkTH_Mo_6tbxM')
bal2 = InlineKeyboardButton(decode('\ud83d\udcb0', 'Яндекс'), callback_data='yandex', url= 'https://www.google.com/search?q=%D0%94%D0%98%D0%9C%D0%90+%D0%9F%D0%98%D0%94%D0%90%D0%A0%D0%90%D0%A1&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi929X-3fX0AhXSk4sKHdh5ClAQ_AUoAXoECAEQAw&biw=1920&bih=969&dpr=1#imgrc=RVkTH_Mo_6tbxM')
pay = InlineKeyboardMarkup().row(bal1).row(bal2)

#ОТЗЫВЫ
ot1 = InlineKeyboardButton('Канал с отзывами', callback_data='ot1', url= 'https://www.google.com/search?q=%D0%94%D0%98%D0%9C%D0%90+%D0%9F%D0%98%D0%94%D0%90%D0%A0%D0%90%D0%A1&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi929X-3fX0AhXSk4sKHdh5ClAQ_AUoAXoECAEQAw&biw=1920&bih=969&dpr=1#imgrc=RVkTH_Mo_6tbxM')
ot = InlineKeyboardMarkup().row(ot1)

#ОСНОВНОЕ МЕНЮ
b1 = KeyboardButton(decode('\ud83d\udce6', 'Товары'))
b2 = KeyboardButton(decode('\ud83d\udda5', 'Кабинет'))
b3 = KeyboardButton(decode('\ud83d\udcb3', 'Мои кошельки'))
b4 = KeyboardButton(decode('\ud83d\udc8c', 'Помощь'))
b5 = KeyboardButton(decode('\ud83d\udc41\u200d\ud83d\udde8', 'Отзывы'))
start_knopki = ReplyKeyboardMarkup(resize_keyboard=True).row(b1, b2).row(b3, b4).row(b5)

#ТОВАРЫ
b1_1 = InlineKeyboardButton(decode('\ud83d\udd38', 'Кошельки Qiwi с балансом'), callback_data='1')
b1_2 = InlineKeyboardButton(decode('\ud83d\udd39', 'Кошельки Qiwi с известным балансом'), callback_data='2')
b1_3 = InlineKeyboardButton(decode('\ud83d\udcc0', 'Программа для подбора кошельков'), callback_data='3')
first_menu = InlineKeyboardMarkup().row(b1_1).row(b1_2).row(b1_3)

b1_1_1 = InlineKeyboardButton(decode('1\ufe0f\u20e3', 'Баланс 800-1400р | Цена: 400'), callback_data='4')
b1_2_2 = InlineKeyboardButton(decode('2\ufe0f\u20e3', 'Qiwi с балансом 3600-5200р | Цена: 1000'), callback_data='5')
b1_3_3 = InlineKeyboardButton(decode('3\ufe0f\u20e3', 'Qiwi с балансом 8600-14200р | Цена: 2400'), callback_data='6')
first_menu_1 = InlineKeyboardMarkup().row(b1_1_1).row(b1_2_2).row(b1_3_3)

b1_1_1_1 = InlineKeyboardButton(decode('1\ufe0f\u20e3', f'Qiwi с балансом 16 957р | Цена: 2645'), callback_data='7')
b1_2_2_2 = InlineKeyboardButton(decode('2\ufe0f\u20e3', f'Qiwi с балансом 32 100р | Цена: 3900'), callback_data='8')
first_menu_2 = InlineKeyboardMarkup().row(b1_1_1_1).row(b1_2_2_2)

b1_1_1_1_1 = InlineKeyboardButton(decode('\u26a0\ufe0f', 'Бессрочная лицензия | Цена: 3990'), callback_data='9')
first_menu_3 = InlineKeyboardMarkup().row(b1_1_1_1_1)