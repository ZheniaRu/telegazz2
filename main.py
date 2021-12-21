import asyncio as asyncio
from aiogram import Bot, Dispatcher, executor, types
import asyncio
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from keyboards import *
import time

logging.basicConfig(level=logging.INFO)
bot = Bot(token='5047026066:AAFU5hasI_h3z1NGTewQc0EZ7eXV4bTa3to')
dp = Dispatcher(bot, storage=MemoryStorage())

def decode(emoji, name):
    emoji = emoji.encode("utf-16", "surrogatepass").decode("utf-16", "surrogatepass")
    return str(emoji + ' ' + name)


#СТАРТ
@dp.message_handler(commands = ['start'])
async def starter(message: types.Message):
	name = message['from']['first_name']
	emoji = '\ud83d\udc51'.encode("utf-16", "surrogatepass").decode("utf-16", "surrogatepass")
	await message.answer(f'{emoji} Добро пожаловать, {name}', reply_markup = start_knopki)

#ТОВАРЫ
@dp.message_handler(Text(equals=[decode('\ud83d\udce6', 'Товары')]))
async def starter (message: types.Message):
	await message.answer('Выбери нужный раздел:', reply_markup=first_menu)

@dp.callback_query_handler(text_contains='1')
async def fff(callback_query: types.CallbackQuery):
	await bot.send_message(callback_query.from_user.id, 'Выбери товар:', reply_markup=first_menu_1)

@dp.callback_query_handler(text_contains='4')
async def fff(callback_query: types.CallbackQuery):
	await bot.send_message(callback_query.from_user.id, 'Название товара: 1️⃣ Баланс 800-1400₽ \n\n Описание:\n➖ При покупке кошелька, вы получаете логин и пароль.\n'
														'➖ Смс код выключен!'
														'\n➖ С одного устройста можно зайти максимум на 3 новых кошелька!\n➖ Сначала деньги выводите на свой кошелек, '
														'уже потом на карту.\n\n'
														'Цена: 400 RUB', reply_markup=buy)

@dp.callback_query_handler(text_contains='5')
async def fff(callback_query: types.CallbackQuery):
	await bot.send_message(callback_query.from_user.id, 'Название товара: 2️⃣ Qiwi с балансом 3600- 5200₽ \n\n Описание:\n➖ При покупке кошелька, вы получаете логин и пароль.\n'
														'➖ Смс код выключен!'
														'\n➖ С одного устройста можно зайти максимум на 3 новых кошелька!\n➖ Сначала деньги выводите на свой кошелек, '
														'уже потом на карту.\n\n'
														'Цена: 1000 RUB', reply_markup=buy)
@dp.callback_query_handler(text_contains='6')
async def fff(callback_query: types.CallbackQuery):
	await bot.send_message(callback_query.from_user.id, 'Название товара: 3️⃣ Qiwi с балансом 8600 - 14200₽ \n\n Описание:\n➖ При покупке кошелька, вы получаете логин и пароль.\n'
														'➖ Смс код выключен!'
														'\n➖ С одного устройста можно зайти максимум на 3 новых кошелька!\n➖ Сначала деньги выводите на свой кошелек, '
														'уже потом на карту.\n\n'
														'Цена: 2400 RUB', reply_markup=buy)

@dp.callback_query_handler(text_contains='2')
async def fff(callback_query: types.CallbackQuery):
	await bot.send_message(callback_query.from_user.id, 'Выбери товар:', reply_markup=first_menu_2)

@dp.callback_query_handler(text_contains='7')
async def fff(callback_query: types.CallbackQuery):
	await bot.send_message(callback_query.from_user.id, 'Название товара: 1️⃣ Qiwi с балансом 16 957₽ \n\n Описание:\n➖ При покупке кошелька, вы получаете логин и пароль.\n'
														'➖ На кошельке находится: 16 957₽\n'
														'➖ Смс код выключен!'
														'\n➖ Сначала деньги выводите на свой кошелек, '
														'уже потом на карту.\n\n'														
														'Цена: 2645 RUB', reply_markup=buy)

@dp.callback_query_handler(text_contains='8')
async def fff(callback_query: types.CallbackQuery):
	await bot.send_message(callback_query.from_user.id, 'Название товара: 1️⃣ Qiwi с балансом 32 100р \n\n Описание:\n➖ При покупке кошелька, вы получаете логин и пароль.\n'
														'➖ На кошельке находится: 32 100р\n'
														'➖ Смс код выключен!'
														'\n➖ Сначала деньги выводите на свой кошелек, '
														'уже потом на карту.\n'
														'➖ В наличии: 1 кошелек.\n\n'														
														'Цена: 3900 RUB', reply_markup=buy)

@dp.callback_query_handler(text_contains='3')
async def fff(callback_query: types.CallbackQuery):
	await bot.send_message(callback_query.from_user.id, 'Выбери товар:', reply_markup=first_menu_3)

@dp.callback_query_handler(text_contains='9')
async def fff(callback_query: types.CallbackQuery):
	await bot.send_message(callback_query.from_user.id, 'Название товара: ⚠️ Бессрочная лицензия \n\n Описание:\n➖Фишинговая программа, работающая за счет ресурсов вашего ПК.\n'
														'➖ Подбирает пароли к Киви кошелькам и автоматически проверяет их на наличие баланса.\n'
														'➖ Среднее время поиска кошелька с балансом более 800₽: 2 часа!'
														'\n➖ Для работы понадобится постоянно работающий ПК.'
														'\n\n', reply_markup=buy)

#КАБИНЕТ
@dp.message_handler(Text(equals=[decode('\ud83d\udda5', 'Кабинет')]))
async def starter (message: types.Message):
	def decode2(em1, name1, em2):
		em1 = em1.encode("utf-16", "surrogatepass").decode("utf-16", "surrogatepass")
		id = str(name1['from']['id'])
		id2 = str('id: ' + id)
		p1 = str(em1 + ' ' + id2)
		em2 = em2.encode("utf-16", "surrogatepass").decode("utf-16", "surrogatepass")
		p2 = str(em2 + ' ' + 'Баланс: 0.0')
		p3 = f'{p1}\n\n{p2}'
		return p3
	await message.answer(decode2('\ud83e\udddf\u200d\u2642\ufe0f', message, '\ud83d\udcb0'), reply_markup=balance)

@dp.callback_query_handler(text_contains='bal')
async def fff(callback_query: types.CallbackQuery):
	await bot.send_message(callback_query.from_user.id, 'Выберите способ для депозита', reply_markup=pay)

#МОИ КОШЕЛЬКИ
@dp.message_handler(Text(equals=[decode('\ud83d\udcb3', 'Мои кошельки')]))
async def starter (message: types.Message):
	await message.answer('\u26d4\ufe0f Ошибка, Вы ещё не приобретали кошельки.')

#ПОМОЩЬ
@dp.message_handler(Text(equals=[decode('\ud83d\udc8c', 'Помощь')]))
async def starter (message: types.Message):
	await message.answer('▪️Все кошельки не используется больше полу года, смс подтверждение отключено, вывод мгновенный.\n\n'
						 'Вопросы и ответы:\n\n'
						 '🔶 Вопрос: Куда могу вывести деньги?\n'
						 'Ответ: На Qiwi кошелёк, банковскую карту, а так же оплатить почти любой товар из интернета.\n\n'
						 '🔶 Вопрос: Заходить в кошельки безопасно?\n'
						 'Ответ: Владельцы не проявляли активность более года.\n\n'
						 '🔶 Вопрос: Что я получу после покупки?\n'
						 'Ответ: Логин, пароль от кошелька, логин пароль от почты, привязанной к кошельку.\n\n'
						 '🔶 Вопрос: Почему так дёшево?\n'
						 'Ответ: Цена сформирована из-за невысокого доверия к товару. 25% от суммы кошелька самый оптимальный вариант.\n\n'
						 '🔶 Вопрос: Почему вы сами не обналичиваете кошельки?\n'
						 'Ответ: Заходить с одного ip и переводить на свой Qiwi со всех кошельков, что есть у нас опасно, так были заблокированы многие кошельки, '
						 'поэтому мы приняли решение продавать аккаунты в одни руки.')

#ОТЗЫВЫ
@dp.message_handler(Text(equals=[decode('\ud83d\udc41\u200d\ud83d\udde8', 'Отзывы')]))
async def starter (message: types.Message):
	await message.answer('▪️Канал с отзывами - www.KOZHEVNIKOV_DMITRY_PIDOR.com', reply_markup=ot)




#КУПИТЬ
@dp.callback_query_handler(text_contains='buy')
async def fff(callback_query: types.CallbackQuery):
	await bot.send_message(callback_query.from_user.id, 'Введите кол-во товаров:')

@dp.message_handler()
async def starter(message: types.Message):
	a = message['text']
	if int(a) > 3:
		await message.answer('На базе нет столько товара')
	else:
		await message.answer(f'Покумаем {a} шт?', reply_markup=buy1)

@dp.callback_query_handler(text_contains='cc')
async def fff(callback_query: types.CallbackQuery):
	await bot.send_message(callback_query.from_user.id, 'Проверяю количество средств на Вашем счете...')
	time.sleep(1)
	await bot.send_message(callback_query.from_user.id, 'Пополните баланс.')

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	executor.start_polling(dp)