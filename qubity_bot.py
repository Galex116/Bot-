# -*- coding: utf-8 -*-
import asyncio
import sqlite3
from aiogram import *
from aiogram import Dispatcher, types, Bot
#Библиотеки asqlite,aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import datetime
import aiosqlite
import logging


logging.basicConfig(level=logging.DEBUG)
BOT_TOKEN  = "1982324804:AAHbX1a1M_B-QCYDuoKZYu-717WJxtDOq2c" # Вставьте свой токен бота, токен берете у @botfather
admin_id = "262098658" # Вставьте айди менеджера или админа, например: "421770530"
bot = Bot(token=BOT_TOKEN, parse_mode='html') # Не трогать!
dp = Dispatcher(bot, storage=MemoryStorage()) # Не трогать!


async def bot_info(bot=bot):
    bot_info = await bot.get_me()
    print(bot_info)


# Для красоты, типо чекаю инфу в терминале, типо крутой))
print(f'\n ~ Bot launched at {datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")} \nBot made by @enganese, PM him in telegram for more! \n\n ~ Если с ботом что-то не так, напишите его разработчику в телеграме @enganese!') # Это тоже для красоты, ну а хули? Почему бы и нет?


class User(StatesGroup): # Стэйты, я задрался комменты ставить, просто не трогайте код, и все!
    number = State()
    number2 = State()
    number3 = State()
    number4 = State()
    question = State()


class Buttons:
    def beginning(): # Начало опроса.
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton('Старт', callback_data='start'))
        return markup
    
    def question_1(): # Первый этап - Единственный вопрос
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1. Один', callback_data='1'),
            types.InlineKeyboardButton('2. 2-7', callback_data='2-4'),
            types.InlineKeyboardButton('3. Более 7', callback_data='2-4'),
            types.InlineKeyboardButton('4. Еще не знаю', callback_data='2-4')
        )
        return markup


    def question_2_1(): # Второй этап - Первый вопрос
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1. Тихий open space', callback_data='open_space'),
            types.InlineKeyboardButton('2. Отдельный офис на сутки', callback_data='office_day'),
            types.InlineKeyboardButton('3. Отдельный офис на долгий срок', callback_data='office_longer'),
            types.InlineKeyboardButton('4. Рабочее место[все включено]', callback_data='work_space')
        )
        return markup


    def question_2_2(): # Второй этап - Второй вопрос
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1. Тихий open space', callback_data='open_space'),
            types.InlineKeyboardButton('2. Отдельный офис на сутки', callback_data='office_day'),
            types.InlineKeyboardButton('3. Отдельный офис на долгий срок', callback_data='office_longer'),
            types.InlineKeyboardButton('4. Мероприятия/переговорки', callback_data='celebrities'),
            types.InlineKeyboardButton('5. Рабочее место[все включено]', callback_data='work_space'),
        )
        return markup

    
    def question_3_1():
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1. До 10 тыс. руб.', callback_data='less-10k'),
            types.InlineKeyboardButton('2. 10-14 тыс. руб.', callback_data='10-14k'),
            types.InlineKeyboardButton('3. 14-18 тыс. руб.', callback_data='14-18k'),
            types.InlineKeyboardButton('4. Более 18 тыс. руб.', callback_data='more-18k')
        )
        return markup

    
    def question_3_2():
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1. До 500 руб.', callback_data='less-500'),
            types.InlineKeyboardButton('2. 500-1000 руб.', callback_data='500-1000'),
            types.InlineKeyboardButton('3. 1000-1500 руб.', callback_data='1000-1500'),
            types.InlineKeyboardButton('4. Более 1500 руб.', callback_data='more-1500')
        )
        return markup

    
    def question_3_3():
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1. До 15 тыс. руб.', callback_data='less-15k'),
            types.InlineKeyboardButton('2. 15-20 тыс. руб.', callback_data='15-20k'),
            types.InlineKeyboardButton('3. 20-25 тыс. руб.', callback_data='20-25k'),
            types.InlineKeyboardButton('4. Более 25 тыс. руб.', callback_data='more-25k')
        )
        return markup


    def question_3_4():
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1. До 400 руб.', callback_data='less-400'),
            types.InlineKeyboardButton('2. 400-600 руб.', callback_data='400-600'),
            types.InlineKeyboardButton('3. 600-1000 руб.', callback_data='600-1000'),
            types.InlineKeyboardButton('4. Более 1000 руб.', callback_data='more-1000')
        )
        return markup

    
    def question_3_5():
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1. До 15 тыс. руб.', callback_data='less-15k2'),
            types.InlineKeyboardButton('2. 15-20 тыс. руб.', callback_data='15-20k2'),
            types.InlineKeyboardButton('3. 20-25 тыс. руб.', callback_data='20-25k2'),
            types.InlineKeyboardButton('4. Более 25 тыс. руб.', callback_data='more-25k2')
        )
        return markup


class Buttons2:
    def beginning(): # Начало опроса.
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton('Старт', callback_data='start'))
        return markup
    
    def question_1(): # Первый этап - Единственный вопрос
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1. Один', callback_data='1_2'),
            types.InlineKeyboardButton('2. 2-7', callback_data='2-4_2'),
            types.InlineKeyboardButton('3. Более 7', callback_data='2-4_2'),
            types.InlineKeyboardButton('4. Еще не знаю', callback_data='2-4_2')
        )
        return markup


    def question_2_1(): # Второй этап - Первый вопрос
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1. Тихий open space', callback_data='open_space_2'),
            types.InlineKeyboardButton('2. Отдельный офис на сутки', callback_data='office_day_2'),
            types.InlineKeyboardButton('3. Отдельный офис на долгий срок', callback_data='office_longer_2'),
            types.InlineKeyboardButton('4. Рабочее место[все включено]', callback_data='work_space_2')
        )
        return markup


    def question_2_2(): # Второй этап - Второй вопрос
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1. Тихий open space', callback_data='open_space_2'),
            types.InlineKeyboardButton('2. Отдельный офис на сутки', callback_data='office_day_2'),
            types.InlineKeyboardButton('3. Отдельный офис на долгий срок', callback_data='office_longer_2'),
            types.InlineKeyboardButton('4. Мероприятия/переговорки', callback_data='celebrities_2'),
            types.InlineKeyboardButton('5. Рабочее место[все включено]', callback_data='work_space_2'),
        )
        return markup

    
    def question_3_1():
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1. До 10 тыс. руб.', callback_data='less-10k_2'),
            types.InlineKeyboardButton('2. 10-14 тыс. руб.', callback_data='10-14k_2'),
            types.InlineKeyboardButton('3. 14-18 тыс. руб.', callback_data='14-18k_2'),
            types.InlineKeyboardButton('4. Более 18 тыс. руб.', callback_data='more-18k_2')
        )
        return markup

    
    def question_3_2():
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1. До 500 руб.', callback_data='less-500_2'),
            types.InlineKeyboardButton('2. 500-1000 руб.', callback_data='500-1000_2'),
            types.InlineKeyboardButton('3. 1000-1500 руб.', callback_data='1000-1500_2'),
            types.InlineKeyboardButton('4. Более 1500 руб.', callback_data='more-1500_2')
        )
        return markup

    
    def question_3_3():
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1. До 15 тыс. руб.', callback_data='less-15k_2'),
            types.InlineKeyboardButton('2. 15-20 тыс. руб.', callback_data='15-20k_2'),
            types.InlineKeyboardButton('3. 20-25 тыс. руб.', callback_data='20-25k_2'),
            types.InlineKeyboardButton('4. Более 25 тыс. руб.', callback_data='more-25k_2')
        )
        return markup


    def question_3_4():
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1. До 400 руб.', callback_data='less-400_2'),
            types.InlineKeyboardButton('2. 400-600 руб.', callback_data='400-600_2'),
            types.InlineKeyboardButton('3. 600-1000 руб.', callback_data='600-1000_2'),
            types.InlineKeyboardButton('4. Более 1000 руб.', callback_data='more-1000_2')
        )
        return markup

    
    def question_3_5():
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton('1. До 15 тыс. руб.', callback_data='less-15k2_2'),
            types.InlineKeyboardButton('2. 15-20 тыс. руб.', callback_data='15-20k2_2'),
            types.InlineKeyboardButton('3. 20-25 тыс. руб.', callback_data='20-25k2_2'),
            types.InlineKeyboardButton('4. Более 25 тыс. руб.', callback_data='more-25k2_2')
        )
        return markup


@dp.callback_query_handler(lambda call: True)
async def calls(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'start':
        await call.message.edit_text(text='<i>Сколько вас человек?</i>', reply_markup=Buttons.question_1())
        
    # PASS AGAIN
     
    # 3.1
    
    if call.data == 'less-10k_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('До 10 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()

    if call.data == '10-14k_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('10-14 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()

    if call.data == '14-18k_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('14-18 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()

    if call.data == 'more-18k_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('Более 18 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()


######################################### 3.2


    if call.data == 'less-500_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('До 500 руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()
            
    if call.data == '500-1000_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('До 500 руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()
            
    if call.data == '1000-1500_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('До 500 руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()
            
    if call.data == 'more-1500_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('До 500 руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()
                

############################################  3.3  


    if call.data == 'less-15k_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('До 15 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()
            
    if call.data == '15-20k_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('15-20 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()
            
    if call.data == '20-25k_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('20-25 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()
            
    if call.data == 'more-25k_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('Более 25 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()
            

############################################  3.4


    if call.data == 'less-400_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('До 400 руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()

                
    if call.data == '400-600_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('400-600 руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()
            
    if call.data == '600-1000_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('600-1000 руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()
            
    if call.data == 'more-1000_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('Более 1000 руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()
            

############################################  3.5


    if call.data == 'less-15k2_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('До 15 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()
            
    if call.data == '15-20k2_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('15-20 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()
            
    if call.data == '20-25k2_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('20-25 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()
            
    if call.data == 'more-25k2_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('Более 25 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Новые данные опроса сохранены</i> \nВведите Ваш новый номер(в формате: 79083080269):')
        st = await User.number4.set()
        await asyncio.sleep(3600)
        await state.finish()
        
    if call.data == '1_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a1 = ?, a1_dt = ?;', ('Один', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", ))
            await con.commit()
        await call.message.edit_text(text='<i>Сколько Вас?</i>' ,reply_markup=Buttons2.question_2_1())

    if call.data == '2-4_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a1 = ?, a1_dt = ? WHERE id = ?', ('2-4', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Что Вы ищете?</i>' ,reply_markup=Buttons2.question_2_2())

    if call.data == 'open_space_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a2 = ?, a2_dt = ? WHERE id = ?', ('Open Space', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Укажите бюджет, который вы готовы выделить на аренду рабочего места в open space на месяц: </i>' ,reply_markup=Buttons2.question_3_1())

    if call.data == 'office_day_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a2 = ?, a2_dt = ? WHERE id = ?', ('Офис на сутки', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Укажите бюджет, который вы готовы выделить на аренду рабочего места в офисе в сутки: </i>' ,reply_markup=Buttons2.question_3_2())

    if call.data == 'office_longer_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a2 = ?, a2_dt = ? WHERE id = ?', ('Офис на долгое время', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Укажите бюджет, который вы готовы выделить на аренду рабочего места в офисе в месяц: </i>' ,reply_markup=Buttons2.question_3_3())

    if call.data == 'celebrities_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a2 = ?, a2_dt = ? WHERE id = ?', ('Мероприятия/переговорки', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Укажите бюджет, который вы готовы выделить на аренду помещения для мероприятия/переговоров в час: </i>' ,reply_markup=Buttons2.question_3_4())

    if call.data == 'work_space_2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a2 = ?, a2_dt = ? WHERE id = ?', ('Рабочее место с форматом все включено', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Укажите бюджет, который вы готовы выделить на аренду рабочего места в формате все включено в месяц: </i>' ,reply_markup=Buttons2.question_3_5())

        
    #### PROD
    
    if call.data == '1':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a1 = ?, a1_dt = ?;', ('Один', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", ))
            await con.commit()
        await call.message.edit_text(text='<i>Что Вы ищете?</i>' ,reply_markup=Buttons.question_2_1())

    if call.data == '2-4':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a1 = ?, a1_dt = ? WHERE id = ?', ('2-4', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Что Вы ищете?</i>' ,reply_markup=Buttons.question_2_2())

    if call.data == 'open_space':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a2 = ?, a2_dt = ? WHERE id = ?', ('Open Space', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Укажите бюджет, который вы готовы выделить на аренду рабочего места в open space на месяц: </i>' ,reply_markup=Buttons.question_3_1())

    if call.data == 'office_day':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a2 = ?, a2_dt = ? WHERE id = ?', ('Офис на сутки', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Укажите бюджет, который вы готовы выделить на аренду рабочего места в офисе в сутки: </i>' ,reply_markup=Buttons.question_3_2())

    if call.data == 'office_longer':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a2 = ?, a2_dt = ? WHERE id = ?', ('Офис на долгое время', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Укажите бюджет, который вы готовы выделить на аренду рабочего места в офисе в месяц: </i>' ,reply_markup=Buttons.question_3_3())

    if call.data == 'celebrities':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a2 = ?, a2_dt = ? WHERE id = ?', ('Мероприятия/переговорки', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Укажите бюджет, который вы готовы выделить на аренду помещения для мероприятия/переговоров в час: </i>' ,reply_markup=Buttons.question_3_4())

    if call.data == 'work_space':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a2 = ?, a2_dt = ? WHERE id = ?', ('Рабочее место с форматом все включено', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>Укажите бюджет, который вы готовы выделить на аренду рабочего места в формате все включено в месяц: </i>' ,reply_markup=Buttons.question_3_5())


################################# 3.1


    if call.data == 'less-10k':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('До 10 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в тихом open space всего за 14.500 руб. в месяц \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()

    if call.data == '10-14k':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('10-14 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в тихом open space всего за 14.500 руб. в месяц \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()

    if call.data == '14-18k':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('14-18 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в тихом open space всего за 14.500 руб. в месяц \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()

    if call.data == 'more-18k':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('Более 18 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в тихом open space всего за 14.500 руб. в месяц \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()


######################################### 3.2


    if call.data == 'less-500':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('До 500 руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в офисе всего за 432 руб. в день \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()
                pass
            
    if call.data == '500-1000':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('До 500 руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в офисе всего за 432 руб. в день \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()
                pass
            
    if call.data == '1000-1500':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('До 500 руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в офисе всего за 432 руб. в день \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()
                pass
            
    if call.data == 'more-1500':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('До 500 руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в офисе всего за 432 руб. в день \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()
                pass
            

############################################  3.3  


    if call.data == 'less-15k':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('До 15 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в офисе всего за 16.000 руб. в день \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()
                pass
            
    if call.data == '15-20k':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('15-20 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в офисе всего за 16.000 руб. в день \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()
                pass
            
    if call.data == '20-25k':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('20-25 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в офисе всего за 16.000 руб. в день \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()
                pass
            
    if call.data == 'more-25k':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('Более 25 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в офисе всего за 16.000 руб. в день \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()
                pass
            

############################################  3.4


    if call.data == 'less-400':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('До 400 руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в офисе всего за 322 руб. в день \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()
                pass
                
    if call.data == '400-600':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('400-600 руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в офисе всего за 322 руб. в день \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()
                pass
            
    if call.data == '600-1000':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('600-1000 руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в офисе всего за 322 руб. в день \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()
                pass
            
    if call.data == 'more-1000':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('Более 1000 руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в офисе всего за 322 руб. в день \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()
                pass
            

############################################  3.5


    if call.data == 'less-15k2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('До 15 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в офисе всего за 18.500 руб. в день \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()
                pass
            
    if call.data == '15-20k2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('15-20 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в офисе всего за 18.500 руб. в день \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()
                pass
            
    if call.data == '20-25k2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('20-25 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в офисе всего за 18.500 руб. в день \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()
                pass
            
    if call.data == 'more-25k2':
        async with aiosqlite.connect('dbase.db') as con:
            conn = await con.cursor()
            await conn.execute('UPDATE users SET a3 = ?, a3_dt = ? WHERE id = ?', ('Более 25 тыс. руб.', f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}", call.from_user.id, ))
            await con.commit()
        await call.message.edit_text(text='<i>У нас есть для вас подходящее место возле станции метро Калужская - новый бизнес-коворкинг с закрепленным рабочим местом в офисе всего за 18.500 руб. в день \n\nОставьте свой номер телефона, чтобы забронировать бесплатный день в коворкинге.</i> \n+ бонус: <b>чек-лист для повышения продуктивности удаленной работы.</b>')
        st = await User.number.set()
        await asyncio.sleep(3600)
        await state.finish()
        async with aiosqlite.connect("dbase.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await call.message.answer('<b>Что Вы упускаете на бесплатном дне в новом коворкинге Qubity Space (м. Калужская)?</b> \n\n<b>612 м2</b> пространство для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении \n - удобное рабочее место в тихом open-space для максимально комфортной работы \n - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1ч) \n - пользование Skype-кабиной для созвонов с шумопоглощением (до 1ч) \n\n - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном \n - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой \n - а еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный wifi \n\nЧтобы попасть на бесплатный тестовый день, Вам осталось только написать свой номер телефона(в формате: 79081234455, без +), чтобы забронировать место \nА если вы сделаете это в ближайшие 24 часа, то мы подарим Вам неограниченное время в переговорной комнате и Skype Room на целый день \n\nНапишите номер телефона ниже - запишитесь на бесплатный день и получите бонус!')
            new_st = await User.number3.set()
            await asyncio.sleep(86400)
            async with aiosqlite.connect("dbase.db") as con:
                con.row_factory = lambda cursor, row: row[0]
                #conn = await con.cursor()
                s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                s = await s.fetchone()
            if not s.isdigit():
                await state.finish()
                pass


@dp.message_handler(state=User.number3, content_types='text')
async def get_numbers(message: types.Message, state: FSMContext):
    #await asyncio.sleep(15)
    #if message:
    if message.text.isdigit():
        if 12 >= len(list(message.text)) >= 10:
            number = await state.update_data(number=message.text)
            
            async with aiosqlite.connect('dbase.db') as con:
                conn = await con.cursor()
                await conn.execute('UPDATE users SET number = ? WHERE id = ?', (str(f'{message.text}'), message.from_user.id, ))
                await con.commit()
                info = await conn.execute('SELECT * FROM users WHERE id = ?', (message.from_user.id, ))
                info = await info.fetchall()
            beh = str(info[0]).replace("(", "").replace(")", "").replace("'", "").split(", ")
            await bot.send_message(chat_id=admin_id, text=f'<b>Время записан в часовом поясе Екатеринбурга(+5)!</b> \nИмя: <code>{message.from_user.first_name}</code> \nФамилия: <code>{message.from_user.last_name}</code> \nНомер: <code>{beh[2]}</code> \nID пользователя: <code>{message.from_user.id}</code> \nЮзернэйм пользователя: <code>@{message.from_user.username}</code> \n\nИнформация о действиях пользователя: \n - Ответ на первый опрос: <b>{beh[3]}</b> \n - Время ответа на первый опрос: <b>{beh[4]} | {beh[5]}</b> \n\n - Ответ на второй опрос: <b>{beh[6]}</b> \n - Время ответа на второй опрос: <b>{beh[7]} | {beh[8]}</b> \n\n - Ответ на третий опрос: <b>{beh[9]}</b> \n - Время ответа на третий опрос: <b>{beh[10]} | {beh[11]}</b> \n\n\n<a href="tg://openmessage?user_id={message.from_user.id}">Перейти к пользователю</a>'.replace("@None", "Отсутствует"), disable_notification=True)
            await state.finish()
            if beh[6] == "Open Space":
                await message.answer('''Спасибо, мы приняли Ваши контактные данные.

Совсем скоро с вами свяжется Ваш менеджер, уточнит детали вашего визита и ответит на ваши вопросы.

Ваш обещанный бонус: 15 идей как фрилансеру разнообразить свои рабочие будни, чтобы 24/7 не сидеть дома

“Что бы мне поделать, только бы не поработать?”
Если работая дома вы не можете сосредоточиться и постоянно откладываете задачи на потом, вот 15 советов, которые помогут вам оставаться продуктивным на фрилансе и не сойти с ума:
Планируйте завтрашний день
Составляйте с вечера список дел на завтра.  Зная свои приоритеты, вы не станете тратить время на ерунду и будете меньше отвлекаться.
Научитесь отключаться от работы
Очень сложно перестать думать о работе, когда дом и офис — одно и то же место. Но это необходимо, чтобы восстановиться и не растерять мотивацию. Например, в нашем коворкинге Qubity Space есть комната для отдыха с удобными креслами и игровая зона с турником, брусьями, гантелями и скакалкой. Здесь вы не только сделаете перерыв, но и сможете подтянуть свою физическую форму.
Работайте в определённой одежде
Да, это работает! Многие психологи считают, что как и атмосфера вокруг, одежда создает ощущение того, что вы на работе. 
Не звходите в соц. сети
Полезно поддерживать профессиональные аккаунты в актуальном состоянии. Но иногда это превращается в бездумный серфинг в интернете и растягивается на несколько часов.
Отчитывайтесь кому-то о дедлайнах
Например, договоритесь с другом или коллегой, что будете оповещать о выполнении какой-то задачи. Стыдно будет признаваться, что вы прокрастинировали и просрочили дедлайн, поэтому вы начнёте больше стараться. В наш коворкинг вы можете приходить с друзьями и даже не придется звонить или писать - вы можете показать результат вживую и спросить совета, если в чем-то неуверены.
Всегда имейте в запасе какую-то механическую работу
Иногда просто нет сил на сложные задачи, требующие творческого подхода или концентрации. На такие случаи составьте список необходимых, но скучных механических дел.
Планируйте отдых
Очень сложно расслабиться, когда рабочее место прямо под боком. Поэтому важно выделять в своём расписании перерывы на отдых. Например, в нашем пространстве есть оборудованная кухня с кофемашиной, куда вы можете отойти, чтобы сделать вкусный кофе и полакомиться фруктами и полезными снеками и еще быстрее восстановить силы. 
Не отвлекайтесь
Находясь дома, где за вами никто не следит, у вас постоянно может возникать желание отвлечься на что-то или на кого-то. И так вы не заметите, как пройдет час или два. В коворкинге Qubity Space вы будете находится в окружении работающих людей, глядя на которых вам не захочется прокрастинировать. А еще там нет домашних дел, а уборку выполняет клининг.
Обустройте рабочее место. 
Для продуктивной работы (и здоровой спины) нужен удобный стол и стул, достаточно света и свежего воздуха. Работать лежа в кровати, конечно, приятно, но до момента пока вас постоянно не будет клонить в сон. В нашем open-space вы можете разместиться как за столом на мягком кресле, так и на мягком диване и кресле мешке. А смена обстановки будет позитивно влиять как на вашу бодрость, так и настроение.
Постоянно общайтесь с людьми
Личное общение трудно переоценить, даже если вы интроверт. Оно даёт новые идеи и просто помогает выбраться из собственного пузыря. В нашем бизнес-коворкинге может одновременно работать до 112 человек - среди них вы точно найдете единомышленника, а, возможно, и будущего друга или партнера.

Эти простые советы помогут  не только справляться с работой проще и быстрее, но и приобрести полезные привычки для вашей повседневной жизни.

Ощутимо повысить продуктивность за 1 день вы сможете на бесплатном посещении нашего коворкинга Qubity Space.

В следующих сообщениях Вы получите больше информации о нашем коворинге.''')
                await asyncio.sleep(86400)
                await message.answer('''Ошибки коворкингов, которые учтены в Qubity Space

Удаленная работа из дома. В 2020 году все люди принудительно узнали, что это такое и ощутили на себе все плюсы и минусы remote work. И если по началу большинству людей нравилась работать дома,  то со временем они начали уставать от однообразия и монотонности. 
Неплохим решением для многих стали коворкинги – центры, в которых арендовать рабочее место может любой желающий.
Бизнесмены, стартаперы, фрилансеры и просто творческие люди поначалу оценили все плюсы работы в таком месте, но в какой-то момент резиденты подобных заведений понимают, что помещения перестают быть друзьями для их бизнеса. И вот почему:
Трудности при проведении встреч
Open-space не самое подходящее место для встречи с партнерами и клиентами. Согласитесь, не очень хочется, чтобы вокруг тебя находились “лишние уши”. Вашему приглашенному может быть неловко, к тому же, большинство считает такой формат встреч непрестижным.
Резиденты коворкинга Qubity Space могут бесплатно воспользоваться оборудованной переговорной с шумоизоляцией, где точно никто не подслушает и не будет мешать. Если у вас несколько встреч подряд и на предыдущей вы задержались или клиент приехал раньше, то наши приветливые администраторы встретят вашего гостя, проводят его в комнату отдыха, где он сможет комфортно подождать.
Шумный open-space
Посетители большинства коворкингов страдают от шума и невозможности сосредоточиться, когда вокруг много людей. 
В нашем пространстве действует система штрафов - если резидент ведет себя шумно и мешает остальным, администратор сделает ему замечание. За 3 замечания резидент попадает в черный список и не имеет права посещать коворкинг 1 месяц.
Нет гарантии безопасности
Посетить коворкинг может любой человек, который заплатил за аренду места.  Но поскольку на этих площадях часто обитают люди с улицы, степень безопасности личных вещей и идей сокращается. 
В Qubity Space каждый резидент имеет собственный локер, может зайти только по карте-ключу и Face ID, все пространство оборудовано камерами, а за порядком следят администраторы.
Несовпадение графиков
Многие коворкинги уже перешли на круглосуточный режим работы, но еще не везде вы можете поработать в любые часы, и приходится подстраиваться.
Если вы арендуете закрепленное место у нас, то вы можете прийти поработать в любое время суток, даже ночью.
Платная техника, кофе, снеки
Коворкинг - место для работы, отдохнуть и поесть можно дома, или, на крайний случай, в ближайшем кафе.
Мы там не считаем - резиденты Qubity Space вместе с удобным рабочим местом получают еще и неограниченный кофе, фрукты и снеки, бесплатно могут пользоваться любой офисной техникой.

В Qubity Space мы пострались развеять все мифы о работе в коворкингах и сделать пространство максимально комфортным для вашей продуктивности. Будем рады видеть вас в числе наших резидентов!''')
                await asyncio.sleep(86400)
                await message.answer('''Дизайнерский ремонт в современном стиле, панорамные окна, собственный спортзал и кухня - видеообзор пространства Qubity Space

Неважно, успели вы посетить наш коворкинг или еще нет, вы можете посмотреть, как выглядит наше пространство внутри в небольшом видео.
Будучи резидентом, вы сможете посещать все эти зоны и использовать все преимущества коворкинга.
Приятного просмотра!''')
                await asyncio.sleep(86400)
                await message.answer('''Почему работая в коворкинге ты намного быстрее станешь лучше как специалист и начнешь больше зарабатывать? - отзыв от резидента Qubity Space

Меня зовут Дмитрий, я занимаюсь созданием сайтов уже более 8 лет, 5 лет из которых я работаю на фрилансе. Изначально, когда ушел из офиса, работал дома или в кофейне неподалеку. Понял, что работа из дома дается мне нелегко - не могу сосредоточиться, а в кофейне шумно и не всегда есть место, где можно сесть.
Поэтому стал искать коворкинг в Москве, чтобы было удобно и недалеко от меня.
За пару лет поменял несколько мест, где-то нравилось больше, где-то меньше, но везде были свои недостатки. Для работы мне важна тишина, удобное рабочее место и круглосуточный доступ, т.к. иногда люблю зависнуть над проектом до 12 ночи. В большинстве коворкингов этого не хватало.
Пару месяцев назад друг посоветовал посетить коворкинг Qubity Space. Подкупило, что он находится недалеко от моего дома (15 минут пешком). Пришел на тестовый день и уже работаю там с июня. Это потрясающее место. Если судить по внешним факторам — это пожалуй лучшее место, что я встречал. Сразу как попадаешь сюда, интерьер очень подкупает. Внутри все очень красиво и аккуратно. Отличные удобные офисные кресла и столы. Еще мне особенно нравится то, что коворкинг расположен в бизнес-центре в окружении разных заведений и с развитой инфраструктурой. Есть большой выбор, куда сходить на обед. К тому же можно перекусить прямо в самом коворкинге - тут есть большая просторная кухня с бесплатным кофе. 
Что еще поразило - это абсолютная тишина, почти как в библиотеке. Штрафы за шум, конечно, жестко, зато дисциплина отличная. 
Здесь есть удобная выделенная переговорная с проектором, чего я не встречал в остальных коворкингах.
Еще огромный плюс в пользу Qubity Space - можно работать круглосуточно, если арендовать закрепленное место или офис. Никто в 20:00 не выгоняет, как было на моем предыдущем опыте.
Еще один момент, нельзя снимать коворкинг посуточно или на неделю. Только на месяц, по словам администраторов, этим ограничением они хотят избежать текучки людей и создать дружественную среду, где люди между собой знакомы. Что ж, цель хорошая.

В общем, это отличное место для работы, особенно если вы устали от “домашнего офиса”. Обстановка настраивает на рабочий лад.''')
                await asyncio.sleep(86400*3)
                media = types.MediaGroup()
                media.attach_photo("https://i.imgur.com/d2JHzX7.jpg")
                media.attach_photo("https://i.imgur.com/C1Nue4Q.jpg")
                media.attach_photo("https://i.imgur.com/9Zkuyo5.jpg", '''От чего зависит успех деловой встречи?Конечно же от обстановки!

Естественно важны и другие факторы, например, ваша подготовка, внешний вид, умение презентовать и договариваться. Но даже это все не поможет, если проводить переговоры в неподходящем месте.
Это мы учли в наших переговорных комнатах, ведь именно по обстановке зачастую партнеры или гости судят о солидности мероприятия в целом.

В комнате для переговоров имеется:
проектор
флип-чарт
стабильный быстрый Wi-Fi

🚪Арендуемая площадь - 18 кв.м.

🎎Зал вмещает до 10 человек, мебель стоит по принципу «Круглый стол», также по запросу возможна «театральная» расстановка кресел.

☕️Для комфортного проведения деловых мероприятий у вас будет неограниченный доступ к напиткам, фруктам и снекам. Также в перерыве вы можете разместиться в удобной конмнате отдыха и передохнуть.

Каждый резидент с закрепленным рабочим местом получает доступ к переговорной совершенно бесплатно и может забранировать ее от 1 ч в день.''')
                await message.bot.send_media_group(message.chat.id, media=media)
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Какое время работы локаций и есть ли парковка - ответили на самые популярные вопросы о коворкинге Qubity Space 

Можно ли приводить гостей, если у меня самого тестовый день? А прийти на него второй раз в другую локацию?
Пробный день в коворкинге создан для того, чтобы вы могли прочувствовать атмосферу работы в Qubity Space. Если вы уже побывали в одной из локаций и хотите поработать в течение дня в другой, обратите внимание на тариф “Гость”. Если вам необходимо провести встречу, рекомендуем рассмотреть возможность аренды переговорных комнат или также воспользоваться тарифом “Гость”, включающим посещение 1 гостя.
Где можно припарковаться? 
В Qubity Space обратите внимание на подземную парковку или наземную парковку БЦ “Нео Гео”. Позвоните администратору коворкинга заранее, чтобы узнать, доступно ли парковочное место в запланированное вами время посещения коворкинга. Также на срок от 1 месяца возможно арендовать парковочное место в БЦ.
У вас в офисах есть мебель? Можно ли привезти свою? 
Каждый офис Qubity Space оборудован столами и креслами в соответствии с количеством рабочих мест в нем. Обустроить кабинет вы можете на своё усмотрение (только не забудьте предварительно оповестить администратора, если вы собираетесь вносить в коворкинг что-то крупногабаритное). Если мы получаем от резидентов большое количество запросов на какой-то определённый тип мебели (например, тумбы), рассматриваем возможность дополнить обустройство рабочих мест. Также мы предоставляем в аренду персональные локеры.
Время работы локаций? 
Для резидентов, выбравших тариф "Резидент" или Smart-офис коворкинг открыт круглосуточно. Для резидентов коворкинга, выбравших тариф “Гость”, – с 8:00 до 20:00, в рабочее время команды локации.
Как осуществляется охрана коворкинга? 
Вход в коворкинг осуществляется строго по пропускам резидентов и Face-ID. Также в офисных пространствах установлены камеры видеонаблюдения, к записям с которых в случае необходимости мы можем обратиться. Каждый резидент получает собственный локер для хранения личных вещей, а за порядком следят администраторы.
Вы предоставляете юридический адрес?
Юридический адрес является дополнительной услугой и предоставляется только арендаторам кабинетов, выбравшим срок аренды от 11 месяцев, а также арендой от 25 мест. Вначале мы заключаем с вами договор субаренды, затем вы оплачиваете услугу, и мы готовим подтверждающие вашу работу в офисном пространстве документы для налоговой.
Как организовать мероприятие на вашей площадке? 
Если вы уже определились с датой, ознакомьтесь со свободными временными окнами у администраторов пространства. Если дата свободна, можно приступать к обсуждению деталей события: какое техническое оснащение для него потребуются, какой формат рассадки предполагается, какое количество гостей вы ожидаете увидеть. Во всех наших локациях действует пропускная система, поэтому не забудьте при регистрации запросить у гостей их полные ФИО.

Если у вас остались вопросы, то вы можете задать их администраторам коворкинга Qubity, написав боту в ответ на это сообщение или по телефону: +7 (926) 911-13-96.''')
                q = await User.question.set()
                await asyncio.sleep(86400*3)
                if not q:
                    await message.answer('''Что можно купить за 450 Р? 2 чашки кофе или 1 день в современном коворкинге Qubity Space и пить кофе в неограниченном количестве

Стоимость размещения в коворкинге зависит от того, арендуете вы незакрепленное место в open space или закрепленное в офисе, а также от времени доступа в коворкинг. 

Наши тарифы:

Гость - 1000 Р/день
Незакрепленное место в openspace
Доступ 1 день (8:00-20:00)
Кофе-брейки
Лаундж-зона (30 мин.)
Skype-room (30 мин.)
Все общие зоны

Резидент Light - 14.500 Р/месяц
Незакрепленное место в openspace
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Резидент Platinum - 18.500 Р/месяц
Закрепленное место в Smart-офисе
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Smart-офис - от 16.000 Р/чел
Индивидуальный Smart-офис
Доступ 24/7
Кофе-брейки
Лаундж-зона (от 1 ч./день)
Skype-room (от 1 ч./день)
Все общие зоны

Приходите на бесплатный день в коворкинге Qubity Space, чтобы подобрать тариф для себя
Переходите по ссылке на наш сайт, чтобы забронировать бесплатное место в коворкинге: http://qubity.space/''')
                    await state.finish()
            # Result message to the user.
            if beh[6] == "Офис на сутки":
                await message.answer('''Спасибо, мы приняли Ваши контактные данные.

Совсем скоро с вами свяжется Ваш менеджер, уточнит детали вашего визита и ответит на ваши вопросы.\n\nВаш обещанный бонус: Как рабочая обстановка помогает бороться с эмоциональным выгоранием и увеличивает продуктивность

Последние тенденции общества направлены на поддержание не только физического, но и ментального здоровья. Так как работа занимает большую часть нашей повседневной жизни, специалисты все чаще жалуются на стресс, хроническую усталость и раздражительность. Психологи называют такое состояние эмоциональным выгоранием. Исследование сервисов HeadHunter и “Доктор рядом” за 2020 год показало, что половина из 2,5 тысяч опрошенных работников испытывают тревогу, чуть меньше опрошенных (48%) из-за переутомления стали эмоционально бесчувственными, работают на автомате и ощущают опустошение при выполнении задач. 45% респондентов испытывают личностное отчуждение по отношению к коллегам.
Если вы тоже замечаете за собой такое состояние или его зачатки, то вот Х советов, которые помогут вам справиться с выгоранием и увеличить продуктивность без смены работы и психотерапевта:
Заботьтесь о своем здоровье. 
Сбалансированно питайтесь, наладьте режим сна, занимайтесь спортом, гуляйте на свежем воздухе и полноценно отдыхайте в выходные.
Научитесь отключаться от работы
Многим людям с “синдромом менеджера” сложно найти время на отдых и отвлечься от работы. Но это необходимо, чтобы восстановиться и не растерять мотивацию. Например, в нашем коворкинге Qubity Space есть комната для отдыха с удобными креслами и игровая зона с турником, брусьями, гантелями и скакалкой. Здесь вы не только сделаете перерыв, но и сможете подтянуть свою физическую форму.
Следите за уровнем стресса
Даже если вам кажется, что стресс - неотъемлимая часть вашей жизни и от него нельзя избавиться, то вы ошибаетесь. Значительно уменьшить его влияние помогут рефлексия, медитация, дыхательные практики, а также смена обстановки. 
Поговорите с тем, кому вы доверяете
Это может быть друг, партнер, родители, коллега. Общение с приятными людьми помогает нам расслабиться, поделиться своими чувствами и эмоциями. В нашем коворкинге вы можете работать вместе с коллегами, а также найти новые знакомства среди сильных специалистов в вашей сфере, которые в будущем могут стать вашими друзьями или партнерами.
Сохраняйте свои личные границы
Если игнорировать собственные эмоции и позволять их постоянно нарушать, то рано или поздно вы сталкнетесь с симптомами выгорания. Чтобы такого не произошло, научитесь говорить нет, сократите контакты с неприятными людьми, уберите все раздражители, особенно на работе. Выбирая для работы офис в коворкинге Qubity Space, вы будете находиться в изолированном пространстве, где вас не будут отвлекать и тревожить, чтобы вы могли сосредоточиться на своих задачах без чужого вмешательства.
Планируйте отдых
Очень сложно расслабиться, когда 24/7 думаете о работе. Поэтому важно выделять в своём расписании перерывы на отдых. Например, в нашем пространстве есть оборудованная кухня с кофемашиной, куда вы можете отойти, чтобы сделать вкусный кофе и перекусить фруктами и полезными снеками и еще быстрее восстановить силы. 
Обустройте рабочее место. 
Для продуктивной работы (и здоровой спины) нужен удобный стол и стул, достаточно света и свежего воздуха. В наших офисах настроена система вентиляции, большие окна и много света, чтобы вы могли чувствовать себя хорошо ментально и физически.

Эти простые советы помогут  не только справиться с симптомами эмоцианального выгорания, но и приобрести полезные привычки для вашей повседневной жизни.

Ощутимо повысить продуктивность за 1 день вы сможете на бесплатном посещении нашего коворкинга Qubity Space.
В следующих сообщениях Вы получите больше информации о нашем коворинге.''')
                await asyncio.sleep(86400)
                await message.answer('''Удаленная работа из дома. В 2020 году все люди принудительно узнали, что это такое и ощутили на себе все плюсы и минусы remote work. И если по началу большинству людей нравилась работать дома,  то со временем они начали уставать от однообразия и монотонности. 
Неплохим решением для многих стали коворкинги – центры, в которых арендовать рабочее место может любой желающий.
Бизнесмены, стартаперы, фрилансеры и просто творческие люди поначалу оценили все плюсы работы в таком месте, но в какой-то момент резиденты подобных заведений понимают, что помещения перестают быть друзьями для их бизнеса. И вот почему:
- Трудности при проведении встреч
Open-space не самое подходящее место для встречи с партнерами и клиентами. Согласитесь, не очень хочется, чтобы вокруг тебя находились “лишние уши”. Вашему приглашенному может быть неловко, к тому же, большинство считает такой формат встреч непрестижным.
Резиденты коворкинга Qubity Space могут бесплатно воспользоваться оборудованной переговорной с шумоизоляцией, где точно никто не подслушает и не будет мешать. Если у вас несколько встреч подряд и на предыдущей вы задержались или клиент приехал раньше, то наши приветливые администраторы встретят вашего гостя, проводят его в комнату отдыха, где он сможет комфортно подождать.
 - Шумный open-space
Посетители большинства коворкингов страдают от шума и невозможности сосредоточиться, когда вокруг много людей. 
В нашем пространстве действует система штрафов - если резидент ведет себя шумно и мешает остальным, администратор сделает ему замечание. За 3 замечания резидент попадает в черный список и не имеет права посещать коворкинг 1 месяц.
 - Нет гарантии безопасности
Посетить коворкинг может любой человек, который заплатил за аренду места.  Но поскольку на этих площадях часто обитают люди с улицы, степень безопасности личных вещей и идей сокращается. 
В Qubity Space каждый резидент имеет собственный локер, может зайти только по карте-ключу и Face ID, все пространство оборудовано камерами, а за порядком следят администраторы.
 - Несовпадение графиков
Многие коворкинги уже перешли на круглосуточный режим работы, но еще не везде вы можете поработать в любые часы, и приходится подстраиваться.
Если вы арендуете закрепленное место у нас, то вы можете прийти поработать в любое время суток, даже ночью.
 - Платная техника, кофе, снеки
Коворкинг - место для работы, отдохнуть и поесть можно дома, или, на крайний случай, в ближайшем кафе.
Мы там не считаем - резиденты Qubity Space вместе с удобным рабочим местом получают еще и неограниченный кофе, фрукты и снеки, бесплатно могут пользоваться любой офисной техникой.

В Qubity Space мы пострались развеять все мифы о работе в коворкингах и сделать пространство максимально комфортным для вашей продуктивности. Будем рады видеть вас в числе наших резидентов!''')
                await asyncio.sleep(86400)
                await message.answer('''Дизайнерский ремонт в современном стиле, панорамные окна, собственный спортзал и кухня - видеообзор пространства Qubity Space

Неважно, успели вы посетить наш коворкинг или еще нет, вы можете посмотреть, как выглядит наше пространство внутри в небольшом видео.
Будучи резидентом, вы сможете посещать все эти зоны и использовать все преимущества коворкинга.
Приятного просмотра!''')
                await asyncio.sleep(86400)
                await message.answer('''Почему работая в коворкинге ты намного быстрее станешь лучше как специалист и начнешь больше зарабатывать? - отзыв от резидента Qubity Space

Меня зовут Дмитрий, я занимаюсь созданием сайтов уже более 8 лет, 5 лет из которых я работаю на фрилансе. Изначально, когда ушел из офиса, работал дома или в кофейне неподалеку. Понял, что работа из дома дается мне нелегко - не могу сосредоточиться, а в кофейне шумно и не всегда есть место, где можно сесть.
Поэтому стал искать коворкинг в Москве, чтобы было удобно и недалеко от меня.
За пару лет поменял несколько мест, где-то нравилось больше, где-то меньше, но везде были свои недостатки. Для работы мне важна тишина, удобное рабочее место и круглосуточный доступ, т.к. иногда люблю зависнуть над проектом до 12 ночи. В большинстве коворкингов этого не хватало.
Пару месяцев назад друг посоветовал посетить коворкинг Qubity Space. Подкупило, что он находится недалеко от моего дома (15 минут пешком). Пришел на тестовый день и уже работаю там с июня. Это потрясающее место. Если судить по внешним факторам — это пожалуй лучшее место, что я встречал. Сразу как попадаешь сюда, интерьер очень подкупает. Внутри все очень красиво и аккуратно. Отличные удобные офисные кресла и столы. Еще мне особенно нравится то, что коворкинг расположен в бизнес-центре в окружении разных заведений и с развитой инфраструктурой. Есть большой выбор, куда сходить на обед. К тому же можно перекусить прямо в самом коворкинге - тут есть большая просторная кухня с бесплатным кофе. 
Что еще поразило - это абсолютная тишина, почти как в библиотеке. Штрафы за шум, конечно, жестко, зато дисциплина отличная. 
Здесь есть удобная выделенная переговорная с проектором, чего я не встречал в остальных коворкингах.
Еще огромный плюс в пользу Qubity Space - можно работать круглосуточно, если арендовать закрепленное место или офис. Никто в 20:00 не выгоняет, как было на моем предыдущем опыте.
Еще один момент, нельзя снимать коворкинг посуточно или на неделю. Только на месяц, по словам администраторов, этим ограничением они хотят избежать текучки людей и создать дружественную среду, где люди между собой знакомы. Что ж, цель хорошая.

В общем, это отличное место для работы, особенно если вы устали от “домашнего офиса”. Обстановка настраивает на рабочий лад.''')
                await asyncio.sleep(86400*3)
                media = types.MediaGroup()
                media.attach_photo("https://i.imgur.com/d2JHzX7.jpg")
                media.attach_photo("https://i.imgur.com/C1Nue4Q.jpg")
                media.attach_photo("https://i.imgur.com/9Zkuyo5.jpg", '''От чего зависит успех деловой встречи?Конечно же от обстановки!

Естественно важны и другие факторы, например, ваша подготовка, внешний вид, умение презентовать и договариваться. Но даже это все не поможет, если проводить переговоры в неподходящем месте.
Это мы учли в наших переговорных комнатах, ведь именно по обстановке зачастую партнеры или гости судят о солидности мероприятия в целом.

В комнате для переговоров имеется:
проектор
флип-чарт
стабильный быстрый Wi-Fi

🚪Арендуемая площадь - 18 кв.м.

🎎Зал вмещает до 10 человек, мебель стоит по принципу «Круглый стол», также по запросу возможна «театральная» расстановка кресел.

☕️Для комфортного проведения деловых мероприятий у вас будет неограниченный доступ к напиткам, фруктам и снекам. Также в перерыве вы можете разместиться в удобной конмнате отдыха и передохнуть.

Каждый резидент с закрепленным рабочим местом получает доступ к переговорной совершенно бесплатно и может забранировать ее от 1 ч в день.''')
                await message.bot.send_media_group(message.chat.id, media=media)
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Какое время работы локаций и есть ли парковка - ответили на самые популярные вопросы о коворкинге Qubity Space 

Можно ли приводить гостей, если у меня самого тестовый день? А прийти на него второй раз в другую локацию?
Пробный день в коворкинге создан для того, чтобы вы могли прочувствовать атмосферу работы в Qubity Space. Если вы уже побывали в одной из локаций и хотите поработать в течение дня в другой, обратите внимание на тариф “Гость”. Если вам необходимо провести встречу, рекомендуем рассмотреть возможность аренды переговорных комнат или также воспользоваться тарифом “Гость”, включающим посещение 1 гостя.
Где можно припарковаться? 
В Qubity Space обратите внимание на подземную парковку или наземную парковку БЦ “Нео Гео”. Позвоните администратору коворкинга заранее, чтобы узнать, доступно ли парковочное место в запланированное вами время посещения коворкинга. Также на срок от 1 месяца возможно арендовать парковочное место в БЦ.
У вас в офисах есть мебель? Можно ли привезти свою? 
Каждый офис Qubity Space оборудован столами и креслами в соответствии с количеством рабочих мест в нем. Обустроить кабинет вы можете на своё усмотрение (только не забудьте предварительно оповестить администратора, если вы собираетесь вносить в коворкинг что-то крупногабаритное). Если мы получаем от резидентов большое количество запросов на какой-то определённый тип мебели (например, тумбы), рассматриваем возможность дополнить обустройство рабочих мест. Также мы предоставляем в аренду персональные локеры.
Время работы локаций? 
Для резидентов, выбравших тариф "Резидент" или Smart-офис коворкинг открыт круглосуточно. Для резидентов коворкинга, выбравших тариф “Гость”, – с 8:00 до 20:00, в рабочее время команды локации.
Как осуществляется охрана коворкинга? 
Вход в коворкинг осуществляется строго по пропускам резидентов и Face-ID. Также в офисных пространствах установлены камеры видеонаблюдения, к записям с которых в случае необходимости мы можем обратиться. Каждый резидент получает собственный локер для хранения личных вещей, а за порядком следят администраторы.
Вы предоставляете юридический адрес?
Юридический адрес является дополнительной услугой и предоставляется только арендаторам кабинетов, выбравшим срок аренды от 11 месяцев, а также арендой от 25 мест. Вначале мы заключаем с вами договор субаренды, затем вы оплачиваете услугу, и мы готовим подтверждающие вашу работу в офисном пространстве документы для налоговой.
Как организовать мероприятие на вашей площадке? 
Если вы уже определились с датой, ознакомьтесь со свободными временными окнами у администраторов пространства. Если дата свободна, можно приступать к обсуждению деталей события: какое техническое оснащение для него потребуются, какой формат рассадки предполагается, какое количество гостей вы ожидаете увидеть. Во всех наших локациях действует пропускная система, поэтому не забудьте при регистрации запросить у гостей их полные ФИО.

Если у вас остались вопросы, то вы можете задать их администраторам коворкинга Qubity, написав боту в ответ на это сообщение или по телефону: +7 (926) 911-13-96.''')
                q = await User.question.set()
                await asyncio.sleep(86400*3)
                if not q:
                    await message.answer('''Что можно купить за 450 Р? 2 чашки кофе или 1 день в современном коворкинге Qubity Space и пить кофе в неограниченном количестве

Стоимость размещения в коворкинге зависит от того, арендуете вы незакрепленное место в open space или закрепленное в офисе, а также от времени доступа в коворкинг. 

Наши тарифы:

Гость - 1000 Р/день
Незакрепленное место в openspace
Доступ 1 день (8:00-20:00)
Кофе-брейки
Лаундж-зона (30 мин.)
Skype-room (30 мин.)
Все общие зоны

Резидент Light - 14.500 Р/месяц
Незакрепленное место в openspace
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Резидент Platinum - 18.500 Р/месяц
Закрепленное место в Smart-офисе
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Smart-офис - от 16.000 Р/чел
Индивидуальный Smart-офис
Доступ 24/7
Кофе-брейки
Лаундж-зона (от 1 ч./день)
Skype-room (от 1 ч./день)
Все общие зоны

Приходите на бесплатный день в коворкинге Qubity Space, чтобы подобрать тариф для себя
Переходите по ссылке на наш сайт, чтобы забронировать бесплатное место в коворкинге: http://qubity.space/''')
                    await state.finish()
            
            if beh[6] == "Офис на долгое время":
                await message.answer('''Спасибо, мы приняли Ваши контактные данные.

Совсем скоро с вами свяжется Ваш менеджер, уточнит детали вашего визита и ответит на ваши вопросы.\n\nВаш обещанный бонус: Как рабочая обстановка помогает бороться с эмоциональным выгоранием и увеличивает продуктивность

Последние тенденции общества направлены на поддержание не только физического, но и ментального здоровья. Так как работа занимает большую часть нашей повседневной жизни, специалисты все чаще жалуются на стресс, хроническую усталость и раздражительность. Психологи называют такое состояние эмоциональным выгоранием. Исследование сервисов HeadHunter и “Доктор рядом” за 2020 год показало, что половина из 2,5 тысяч опрошенных работников испытывают тревогу, чуть меньше опрошенных (48%) из-за переутомления стали эмоционально бесчувственными, работают на автомате и ощущают опустошение при выполнении задач. 45% респондентов испытывают личностное отчуждение по отношению к коллегам.
Если вы тоже замечаете за собой такое состояние или его зачатки, то вот Х советов, которые помогут вам справиться с выгоранием и увеличить продуктивность без смены работы и психотерапевта:
Заботьтесь о своем здоровье. 
Сбалансированно питайтесь, наладьте режим сна, занимайтесь спортом, гуляйте на свежем воздухе и полноценно отдыхайте в выходные.
Научитесь отключаться от работы
Многим людям с “синдромом менеджера” сложно найти время на отдых и отвлечься от работы. Но это необходимо, чтобы восстановиться и не растерять мотивацию. Например, в нашем коворкинге Qubity Space есть комната для отдыха с удобными креслами и игровая зона с турником, брусьями, гантелями и скакалкой. Здесь вы не только сделаете перерыв, но и сможете подтянуть свою физическую форму.
Следите за уровнем стресса
Даже если вам кажется, что стресс - неотъемлимая часть вашей жизни и от него нельзя избавиться, то вы ошибаетесь. Значительно уменьшить его влияние помогут рефлексия, медитация, дыхательные практики, а также смена обстановки. 
Поговорите с тем, кому вы доверяете
Это может быть друг, партнер, родители, коллега. Общение с приятными людьми помогает нам расслабиться, поделиться своими чувствами и эмоциями. В нашем коворкинге вы можете работать вместе с коллегами, а также найти новые знакомства среди сильных специалистов в вашей сфере, которые в будущем могут стать вашими друзьями или партнерами.
Сохраняйте свои личные границы
Если игнорировать собственные эмоции и позволять их постоянно нарушать, то рано или поздно вы сталкнетесь с симптомами выгорания. Чтобы такого не произошло, научитесь говорить нет, сократите контакты с неприятными людьми, уберите все раздражители, особенно на работе. Выбирая для работы офис в коворкинге Qubity Space, вы будете находиться в изолированном пространстве, где вас не будут отвлекать и тревожить, чтобы вы могли сосредоточиться на своих задачах без чужого вмешательства.
Планируйте отдых
Очень сложно расслабиться, когда 24/7 думаете о работе. Поэтому важно выделять в своём расписании перерывы на отдых. Например, в нашем пространстве есть оборудованная кухня с кофемашиной, куда вы можете отойти, чтобы сделать вкусный кофе и перекусить фруктами и полезными снеками и еще быстрее восстановить силы. 
Обустройте рабочее место. 
Для продуктивной работы (и здоровой спины) нужен удобный стол и стул, достаточно света и свежего воздуха. В наших офисах настроена система вентиляции, большие окна и много света, чтобы вы могли чувствовать себя хорошо ментально и физически.

Эти простые советы помогут  не только справиться с симптомами эмоцианального выгорания, но и приобрести полезные привычки для вашей повседневной жизни.

Ощутимо повысить продуктивность за 1 день вы сможете на бесплатном посещении нашего коворкинга Qubity Space.
В следующих сообщениях Вы получите больше информации о нашем коворинге.''')
                await asyncio.sleep(86400)
                await message.answer('''Удаленная работа из дома. В 2020 году все люди принудительно узнали, что это такое и ощутили на себе все плюсы и минусы remote work. И если по началу большинству людей нравилась работать дома,  то со временем они начали уставать от однообразия и монотонности. 
Неплохим решением для многих стали коворкинги – центры, в которых арендовать рабочее место может любой желающий.
Бизнесмены, стартаперы, фрилансеры и просто творческие люди поначалу оценили все плюсы работы в таком месте, но в какой-то момент резиденты подобных заведений понимают, что помещения перестают быть друзьями для их бизнеса. И вот почему:
- Трудности при проведении встреч
Open-space не самое подходящее место для встречи с партнерами и клиентами. Согласитесь, не очень хочется, чтобы вокруг тебя находились “лишние уши”. Вашему приглашенному может быть неловко, к тому же, большинство считает такой формат встреч непрестижным.
Резиденты коворкинга Qubity Space могут бесплатно воспользоваться оборудованной переговорной с шумоизоляцией, где точно никто не подслушает и не будет мешать. Если у вас несколько встреч подряд и на предыдущей вы задержались или клиент приехал раньше, то наши приветливые администраторы встретят вашего гостя, проводят его в комнату отдыха, где он сможет комфортно подождать.
 - Шумный open-space
Посетители большинства коворкингов страдают от шума и невозможности сосредоточиться, когда вокруг много людей. 
В нашем пространстве действует система штрафов - если резидент ведет себя шумно и мешает остальным, администратор сделает ему замечание. За 3 замечания резидент попадает в черный список и не имеет права посещать коворкинг 1 месяц.
 - Нет гарантии безопасности
Посетить коворкинг может любой человек, который заплатил за аренду места.  Но поскольку на этих площадях часто обитают люди с улицы, степень безопасности личных вещей и идей сокращается. 
В Qubity Space каждый резидент имеет собственный локер, может зайти только по карте-ключу и Face ID, все пространство оборудовано камерами, а за порядком следят администраторы.
 - Несовпадение графиков
Многие коворкинги уже перешли на круглосуточный режим работы, но еще не везде вы можете поработать в любые часы, и приходится подстраиваться.
Если вы арендуете закрепленное место у нас, то вы можете прийти поработать в любое время суток, даже ночью.
 - Платная техника, кофе, снеки
Коворкинг - место для работы, отдохнуть и поесть можно дома, или, на крайний случай, в ближайшем кафе.
Мы там не считаем - резиденты Qubity Space вместе с удобным рабочим местом получают еще и неограниченный кофе, фрукты и снеки, бесплатно могут пользоваться любой офисной техникой.

В Qubity Space мы пострались развеять все мифы о работе в коворкингах и сделать пространство максимально комфортным для вашей продуктивности. Будем рады видеть вас в числе наших резидентов!''')
                await asyncio.sleep(86400)
                await message.answer('''Дизайнерский ремонт в современном стиле, панорамные окна, собственный спортзал и кухня - видеообзор пространства Qubity Space

Неважно, успели вы посетить наш коворкинг или еще нет, вы можете посмотреть, как выглядит наше пространство внутри в небольшом видео.
Будучи резидентом, вы сможете посещать все эти зоны и использовать все преимущества коворкинга.
Приятного просмотра!''')
                await asyncio.sleep(86400)
                await message.answer('''Почему работая в коворкинге ты намного быстрее станешь лучше как специалист и начнешь больше зарабатывать? - отзыв от резидента Qubity Space

Меня зовут Дмитрий, я занимаюсь созданием сайтов уже более 8 лет, 5 лет из которых я работаю на фрилансе. Изначально, когда ушел из офиса, работал дома или в кофейне неподалеку. Понял, что работа из дома дается мне нелегко - не могу сосредоточиться, а в кофейне шумно и не всегда есть место, где можно сесть.
Поэтому стал искать коворкинг в Москве, чтобы было удобно и недалеко от меня.
За пару лет поменял несколько мест, где-то нравилось больше, где-то меньше, но везде были свои недостатки. Для работы мне важна тишина, удобное рабочее место и круглосуточный доступ, т.к. иногда люблю зависнуть над проектом до 12 ночи. В большинстве коворкингов этого не хватало.
Пару месяцев назад друг посоветовал посетить коворкинг Qubity Space. Подкупило, что он находится недалеко от моего дома (15 минут пешком). Пришел на тестовый день и уже работаю там с июня. Это потрясающее место. Если судить по внешним факторам — это пожалуй лучшее место, что я встречал. Сразу как попадаешь сюда, интерьер очень подкупает. Внутри все очень красиво и аккуратно. Отличные удобные офисные кресла и столы. Еще мне особенно нравится то, что коворкинг расположен в бизнес-центре в окружении разных заведений и с развитой инфраструктурой. Есть большой выбор, куда сходить на обед. К тому же можно перекусить прямо в самом коворкинге - тут есть большая просторная кухня с бесплатным кофе. 
Что еще поразило - это абсолютная тишина, почти как в библиотеке. Штрафы за шум, конечно, жестко, зато дисциплина отличная. 
Здесь есть удобная выделенная переговорная с проектором, чего я не встречал в остальных коворкингах.
Еще огромный плюс в пользу Qubity Space - можно работать круглосуточно, если арендовать закрепленное место или офис. Никто в 20:00 не выгоняет, как было на моем предыдущем опыте.
Еще один момент, нельзя снимать коворкинг посуточно или на неделю. Только на месяц, по словам администраторов, этим ограничением они хотят избежать текучки людей и создать дружественную среду, где люди между собой знакомы. Что ж, цель хорошая.

В общем, это отличное место для работы, особенно если вы устали от “домашнего офиса”. Обстановка настраивает на рабочий лад.''')
                await asyncio.sleep(86400*3)
                media = types.MediaGroup()
                media.attach_photo("https://i.imgur.com/d2JHzX7.jpg")
                media.attach_photo("https://i.imgur.com/C1Nue4Q.jpg")
                media.attach_photo("https://i.imgur.com/9Zkuyo5.jpg", '''От чего зависит успех деловой встречи?Конечно же от обстановки!

Естественно важны и другие факторы, например, ваша подготовка, внешний вид, умение презентовать и договариваться. Но даже это все не поможет, если проводить переговоры в неподходящем месте.
Это мы учли в наших переговорных комнатах, ведь именно по обстановке зачастую партнеры или гости судят о солидности мероприятия в целом.

В комнате для переговоров имеется:
проектор
флип-чарт
стабильный быстрый Wi-Fi

🚪Арендуемая площадь - 18 кв.м.

🎎Зал вмещает до 10 человек, мебель стоит по принципу «Круглый стол», также по запросу возможна «театральная» расстановка кресел.

☕️Для комфортного проведения деловых мероприятий у вас будет неограниченный доступ к напиткам, фруктам и снекам. Также в перерыве вы можете разместиться в удобной конмнате отдыха и передохнуть.

Каждый резидент с закрепленным рабочим местом получает доступ к переговорной совершенно бесплатно и может забранировать ее от 1 ч в день.''')
                await message.bot.send_media_group(message.chat.id, media=media)
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Какое время работы локаций и есть ли парковка - ответили на самые популярные вопросы о коворкинге Qubity Space 

Можно ли приводить гостей, если у меня самого тестовый день? А прийти на него второй раз в другую локацию?
Пробный день в коворкинге создан для того, чтобы вы могли прочувствовать атмосферу работы в Qubity Space. Если вы уже побывали в одной из локаций и хотите поработать в течение дня в другой, обратите внимание на тариф “Гость”. Если вам необходимо провести встречу, рекомендуем рассмотреть возможность аренды переговорных комнат или также воспользоваться тарифом “Гость”, включающим посещение 1 гостя.
Где можно припарковаться? 
В Qubity Space обратите внимание на подземную парковку или наземную парковку БЦ “Нео Гео”. Позвоните администратору коворкинга заранее, чтобы узнать, доступно ли парковочное место в запланированное вами время посещения коворкинга. Также на срок от 1 месяца возможно арендовать парковочное место в БЦ.
У вас в офисах есть мебель? Можно ли привезти свою? 
Каждый офис Qubity Space оборудован столами и креслами в соответствии с количеством рабочих мест в нем. Обустроить кабинет вы можете на своё усмотрение (только не забудьте предварительно оповестить администратора, если вы собираетесь вносить в коворкинг что-то крупногабаритное). Если мы получаем от резидентов большое количество запросов на какой-то определённый тип мебели (например, тумбы), рассматриваем возможность дополнить обустройство рабочих мест. Также мы предоставляем в аренду персональные локеры.
Время работы локаций? 
Для резидентов, выбравших тариф "Резидент" или Smart-офис коворкинг открыт круглосуточно. Для резидентов коворкинга, выбравших тариф “Гость”, – с 8:00 до 20:00, в рабочее время команды локации.
Как осуществляется охрана коворкинга? 
Вход в коворкинг осуществляется строго по пропускам резидентов и Face-ID. Также в офисных пространствах установлены камеры видеонаблюдения, к записям с которых в случае необходимости мы можем обратиться. Каждый резидент получает собственный локер для хранения личных вещей, а за порядком следят администраторы.
Вы предоставляете юридический адрес?
Юридический адрес является дополнительной услугой и предоставляется только арендаторам кабинетов, выбравшим срок аренды от 11 месяцев, а также арендой от 25 мест. Вначале мы заключаем с вами договор субаренды, затем вы оплачиваете услугу, и мы готовим подтверждающие вашу работу в офисном пространстве документы для налоговой.
Как организовать мероприятие на вашей площадке? 
Если вы уже определились с датой, ознакомьтесь со свободными временными окнами у администраторов пространства. Если дата свободна, можно приступать к обсуждению деталей события: какое техническое оснащение для него потребуются, какой формат рассадки предполагается, какое количество гостей вы ожидаете увидеть. Во всех наших локациях действует пропускная система, поэтому не забудьте при регистрации запросить у гостей их полные ФИО.

Если у вас остались вопросы, то вы можете задать их администраторам коворкинга Qubity, написав боту в ответ на это сообщение или по телефону: +7 (926) 911-13-96.''')
                q = await User.question.set()
                await asyncio.sleep(86400*3)
                if not q:
                    await message.answer('''Что можно купить за 450 Р? 2 чашки кофе или 1 день в современном коворкинге Qubity Space и пить кофе в неограниченном количестве

Стоимость размещения в коворкинге зависит от того, арендуете вы незакрепленное место в open space или закрепленное в офисе, а также от времени доступа в коворкинг. 

Наши тарифы:

Гость - 1000 Р/день
Незакрепленное место в openspace
Доступ 1 день (8:00-20:00)
Кофе-брейки
Лаундж-зона (30 мин.)
Skype-room (30 мин.)
Все общие зоны

Резидент Light - 14.500 Р/месяц
Незакрепленное место в openspace
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Резидент Platinum - 18.500 Р/месяц
Закрепленное место в Smart-офисе
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Smart-офис - от 16.000 Р/чел
Индивидуальный Smart-офис
Доступ 24/7
Кофе-брейки
Лаундж-зона (от 1 ч./день)
Skype-room (от 1 ч./день)
Все общие зоны

Приходите на бесплатный день в коворкинге Qubity Space, чтобы подобрать тариф для себя
Переходите по ссылке на наш сайт, чтобы забронировать бесплатное место в коворкинге: http://qubity.space/''')
                    await state.finish()
            
            if beh[6] == "Мероприятия/переговорки":
                await message.answer('''Спасибо, мы приняли Ваши контактные данные.

Совсем скоро с вами свяжется Ваш менеджер, уточнит детали вашего визита и ответит на ваши вопросы.

Ваш обещанный бонус: Как выбрать помещение, чтобы повысить эффективность тренингов и переговоров?

Конечно, у плохого танцора, помехи никак не связаны с профессионализмом. Тренинг можно провести в любых условиях:
 - и в подвальном банкетном зале,
 - и в зале ресторана,
 - и параллельно обслуживая клиентов…
Любой раздражающий фактор можно минимизировать, но нужна ли эта борьба на ровном месте?

Вот несколько моментов, на которые стоит обратить внимание, выбирая, где провести тренинг:

Изолированное. Посетители и звонки должны остаться за дверью.
Тихое. Стройка за окном, шум оборудования, музыка за стенкой, работающая пожарная сигнализация – не лучший аккомпанемент. Акустику тоже лучше проверить заранее.
Комфортное. 20 градусов чистого воздуха – то, что надо. Тепло зимой, прохладно летом. Работающая вентиляция или возможность открыть окно. Кондиционер и жалюзи летом.
Светлое. Света должно быть достаточно, чтобы читать, меньшая освещённость загоняет в спячку. Отсутствие окон – сильный недостаток, люди быстрее устают.
Просторное. Нужно без помех посадить всех участников полукругом, чтобы с любого места было нормально видно доску, экран. Никаких школьных парт.
Оборудованное всем необходимым. Чаще всего может понадобиться флипчарт, проектор, маркеры. Это можно принести и самому, но будет лучше, если вам не придется переживать, что вы что-то забыли.

Хороший ланч вряд ли вытянет провальный тренинг, зато его отсутствие — испортит даже самую прекрасную программу. Учесть стоит всё:
Организация обедов.
Если имеем дело с доставкой, важно, чтобы привезли вовремя, иначе ломается весь график.
Кофе-брейки.
Идеальное место для кофе-брейка – соседняя комната, а вот кулер или запас бутылок с водой должны быть непосредственно в зале. Необходимость перейти на другой этаж, чтобы попить кофе, сразу превращает 15-минутный перерыв в получасовой. 
Указатели, если не все участники знают дорогу.

В нашем коворкинге есть большая переговорная комната на 30 человек. Она оборудована всем необходимым для комфортного проведения тренингов и переговоров: здесь есть проектор, флипчарт, удобные столы и стулья, шумоизоляция и большие панорамные окна. Также ввм не придется переживать о бизнес-ланчах и перекусах - в пространстве есть удобная кухня с бесплатным кофе и снеками, а для заказа обеда можно вызвать курьера.

Эти простые советы помогут не только подобрать помещение для тренинга, но и увеличить его эффективность и уменьшить время и средства на подготовку.

Оценить наше помещение для переговоров в Qubity Space вы сможете на бесплатном посещении.''')
                await asyncio.sleep(86400)
                await message.answer('''Удаленная работа из дома. В 2020 году все люди принудительно узнали, что это такое и ощутили на себе все плюсы и минусы remote work. И если по началу большинству людей нравилась работать дома,  то со временем они начали уставать от однообразия и монотонности. 
Неплохим решением для многих стали коворкинги – центры, в которых арендовать рабочее место может любой желающий.
Бизнесмены, стартаперы, фрилансеры и просто творческие люди поначалу оценили все плюсы работы в таком месте, но в какой-то момент резиденты подобных заведений понимают, что помещения перестают быть друзьями для их бизнеса. И вот почему:
- Трудности при проведении встреч
Open-space не самое подходящее место для встречи с партнерами и клиентами. Согласитесь, не очень хочется, чтобы вокруг тебя находились “лишние уши”. Вашему приглашенному может быть неловко, к тому же, большинство считает такой формат встреч непрестижным.
Резиденты коворкинга Qubity Space могут бесплатно воспользоваться оборудованной переговорной с шумоизоляцией, где точно никто не подслушает и не будет мешать. Если у вас несколько встреч подряд и на предыдущей вы задержались или клиент приехал раньше, то наши приветливые администраторы встретят вашего гостя, проводят его в комнату отдыха, где он сможет комфортно подождать.
 - Шумный open-space
Посетители большинства коворкингов страдают от шума и невозможности сосредоточиться, когда вокруг много людей. 
В нашем пространстве действует система штрафов - если резидент ведет себя шумно и мешает остальным, администратор сделает ему замечание. За 3 замечания резидент попадает в черный список и не имеет права посещать коворкинг 1 месяц.
 - Нет гарантии безопасности
Посетить коворкинг может любой человек, который заплатил за аренду места.  Но поскольку на этих площадях часто обитают люди с улицы, степень безопасности личных вещей и идей сокращается. 
В Qubity Space каждый резидент имеет собственный локер, может зайти только по карте-ключу и Face ID, все пространство оборудовано камерами, а за порядком следят администраторы.
 - Несовпадение графиков
Многие коворкинги уже перешли на круглосуточный режим работы, но еще не везде вы можете поработать в любые часы, и приходится подстраиваться.
Если вы арендуете закрепленное место у нас, то вы можете прийти поработать в любое время суток, даже ночью.
 - Платная техника, кофе, снеки
Коворкинг - место для работы, отдохнуть и поесть можно дома, или, на крайний случай, в ближайшем кафе.
Мы там не считаем - резиденты Qubity Space вместе с удобным рабочим местом получают еще и неограниченный кофе, фрукты и снеки, бесплатно могут пользоваться любой офисной техникой.

В Qubity Space мы пострались развеять все мифы о работе в коворкингах и сделать пространство максимально комфортным для вашей продуктивности. Будем рады видеть вас в числе наших резидентов!''')
                await asyncio.sleep(86400)
                await message.answer('''Дизайнерский ремонт в современном стиле, панорамные окна, собственный спортзал и кухня - видеообзор пространства Qubity Space

Неважно, успели вы посетить наш коворкинг или еще нет, вы можете посмотреть, как выглядит наше пространство внутри в небольшом видео.
Будучи резидентом, вы сможете посещать все эти зоны и использовать все преимущества коворкинга.
Приятного просмотра!''')
                await asyncio.sleep(86400)
                await message.answer('''Почему работая в коворкинге ты намного быстрее станешь лучше как специалист и начнешь больше зарабатывать? - отзыв от резидента Qubity Space

Меня зовут Дмитрий, я занимаюсь созданием сайтов уже более 8 лет, 5 лет из которых я работаю на фрилансе. Изначально, когда ушел из офиса, работал дома или в кофейне неподалеку. Понял, что работа из дома дается мне нелегко - не могу сосредоточиться, а в кофейне шумно и не всегда есть место, где можно сесть.
Поэтому стал искать коворкинг в Москве, чтобы было удобно и недалеко от меня.
За пару лет поменял несколько мест, где-то нравилось больше, где-то меньше, но везде были свои недостатки. Для работы мне важна тишина, удобное рабочее место и круглосуточный доступ, т.к. иногда люблю зависнуть над проектом до 12 ночи. В большинстве коворкингов этого не хватало.
Пару месяцев назад друг посоветовал посетить коворкинг Qubity Space. Подкупило, что он находится недалеко от моего дома (15 минут пешком). Пришел на тестовый день и уже работаю там с июня. Это потрясающее место. Если судить по внешним факторам — это пожалуй лучшее место, что я встречал. Сразу как попадаешь сюда, интерьер очень подкупает. Внутри все очень красиво и аккуратно. Отличные удобные офисные кресла и столы. Еще мне особенно нравится то, что коворкинг расположен в бизнес-центре в окружении разных заведений и с развитой инфраструктурой. Есть большой выбор, куда сходить на обед. К тому же можно перекусить прямо в самом коворкинге - тут есть большая просторная кухня с бесплатным кофе. 
Что еще поразило - это абсолютная тишина, почти как в библиотеке. Штрафы за шум, конечно, жестко, зато дисциплина отличная. 
Здесь есть удобная выделенная переговорная с проектором, чего я не встречал в остальных коворкингах.
Еще огромный плюс в пользу Qubity Space - можно работать круглосуточно, если арендовать закрепленное место или офис. Никто в 20:00 не выгоняет, как было на моем предыдущем опыте.
Еще один момент, нельзя снимать коворкинг посуточно или на неделю. Только на месяц, по словам администраторов, этим ограничением они хотят избежать текучки людей и создать дружественную среду, где люди между собой знакомы. Что ж, цель хорошая.

В общем, это отличное место для работы, особенно если вы устали от “домашнего офиса”. Обстановка настраивает на рабочий лад.''')
                await asyncio.sleep(86400*3)
                media = types.MediaGroup()
                media.attach_photo("https://i.imgur.com/d2JHzX7.jpg")
                media.attach_photo("https://i.imgur.com/C1Nue4Q.jpg")
                media.attach_photo("https://i.imgur.com/9Zkuyo5.jpg", '''От чего зависит успех деловой встречи?Конечно же от обстановки!

Естественно важны и другие факторы, например, ваша подготовка, внешний вид, умение презентовать и договариваться. Но даже это все не поможет, если проводить переговоры в неподходящем месте.
Это мы учли в наших переговорных комнатах, ведь именно по обстановке зачастую партнеры или гости судят о солидности мероприятия в целом.

В комнате для переговоров имеется:
проектор
флип-чарт
стабильный быстрый Wi-Fi

🚪Арендуемая площадь - 18 кв.м.

🎎Зал вмещает до 10 человек, мебель стоит по принципу «Круглый стол», также по запросу возможна «театральная» расстановка кресел.

☕️Для комфортного проведения деловых мероприятий у вас будет неограниченный доступ к напиткам, фруктам и снекам. Также в перерыве вы можете разместиться в удобной конмнате отдыха и передохнуть.

Каждый резидент с закрепленным рабочим местом получает доступ к переговорной совершенно бесплатно и может забранировать ее от 1 ч в день.''')
                await message.bot.send_media_group(message.chat.id, media=media)
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Какое время работы локаций и есть ли парковка - ответили на самые популярные вопросы о коворкинге Qubity Space 

Можно ли приводить гостей, если у меня самого тестовый день? А прийти на него второй раз в другую локацию?
Пробный день в коворкинге создан для того, чтобы вы могли прочувствовать атмосферу работы в Qubity Space. Если вы уже побывали в одной из локаций и хотите поработать в течение дня в другой, обратите внимание на тариф “Гость”. Если вам необходимо провести встречу, рекомендуем рассмотреть возможность аренды переговорных комнат или также воспользоваться тарифом “Гость”, включающим посещение 1 гостя.
Где можно припарковаться? 
В Qubity Space обратите внимание на подземную парковку или наземную парковку БЦ “Нео Гео”. Позвоните администратору коворкинга заранее, чтобы узнать, доступно ли парковочное место в запланированное вами время посещения коворкинга. Также на срок от 1 месяца возможно арендовать парковочное место в БЦ.
У вас в офисах есть мебель? Можно ли привезти свою? 
Каждый офис Qubity Space оборудован столами и креслами в соответствии с количеством рабочих мест в нем. Обустроить кабинет вы можете на своё усмотрение (только не забудьте предварительно оповестить администратора, если вы собираетесь вносить в коворкинг что-то крупногабаритное). Если мы получаем от резидентов большое количество запросов на какой-то определённый тип мебели (например, тумбы), рассматриваем возможность дополнить обустройство рабочих мест. Также мы предоставляем в аренду персональные локеры.
Время работы локаций? 
Для резидентов, выбравших тариф "Резидент" или Smart-офис коворкинг открыт круглосуточно. Для резидентов коворкинга, выбравших тариф “Гость”, – с 8:00 до 20:00, в рабочее время команды локации.
Как осуществляется охрана коворкинга? 
Вход в коворкинг осуществляется строго по пропускам резидентов и Face-ID. Также в офисных пространствах установлены камеры видеонаблюдения, к записям с которых в случае необходимости мы можем обратиться. Каждый резидент получает собственный локер для хранения личных вещей, а за порядком следят администраторы.
Вы предоставляете юридический адрес?
Юридический адрес является дополнительной услугой и предоставляется только арендаторам кабинетов, выбравшим срок аренды от 11 месяцев, а также арендой от 25 мест. Вначале мы заключаем с вами договор субаренды, затем вы оплачиваете услугу, и мы готовим подтверждающие вашу работу в офисном пространстве документы для налоговой.
Как организовать мероприятие на вашей площадке? 
Если вы уже определились с датой, ознакомьтесь со свободными временными окнами у администраторов пространства. Если дата свободна, можно приступать к обсуждению деталей события: какое техническое оснащение для него потребуются, какой формат рассадки предполагается, какое количество гостей вы ожидаете увидеть. Во всех наших локациях действует пропускная система, поэтому не забудьте при регистрации запросить у гостей их полные ФИО.

Если у вас остались вопросы, то вы можете задать их администраторам коворкинга Qubity, написав боту в ответ на это сообщение или по телефону: +7 (926) 911-13-96.''')
                q = await User.question.set()
                await asyncio.sleep(86400*3)
                if not q:
                    await message.answer('''Что можно купить за 450 Р? 2 чашки кофе или 1 день в современном коворкинге Qubity Space и пить кофе в неограниченном количестве

Стоимость размещения в коворкинге зависит от того, арендуете вы незакрепленное место в open space или закрепленное в офисе, а также от времени доступа в коворкинг. 

Наши тарифы:

Гость - 1000 Р/день
Незакрепленное место в openspace
Доступ 1 день (8:00-20:00)
Кофе-брейки
Лаундж-зона (30 мин.)
Skype-room (30 мин.)
Все общие зоны

Резидент Light - 14.500 Р/месяц
Незакрепленное место в openspace
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Резидент Platinum - 18.500 Р/месяц
Закрепленное место в Smart-офисе
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Smart-офис - от 16.000 Р/чел
Индивидуальный Smart-офис
Доступ 24/7
Кофе-брейки
Лаундж-зона (от 1 ч./день)
Skype-room (от 1 ч./день)
Все общие зоны

Приходите на бесплатный день в коворкинге Qubity Space, чтобы подобрать тариф для себя
Переходите по ссылке на наш сайт, чтобы забронировать бесплатное место в коворкинге: http://qubity.space/''')
                    await state.finish()
            
            if beh[6] == "Рабочее место с форматом все включено":
                await message.answer('''Спасибо, мы приняли Ваши контактные данные.

Совсем скоро с вами свяжется Ваш менеджер, уточнит детали вашего визита и ответит на ваши вопросы.\n\nВаш обещанный бонус: Как рабочая обстановка помогает бороться с эмоциональным выгоранием и увеличивает продуктивность

Последние тенденции общества направлены на поддержание не только физического, но и ментального здоровья. Так как работа занимает большую часть нашей повседневной жизни, специалисты все чаще жалуются на стресс, хроническую усталость и раздражительность. Психологи называют такое состояние эмоциональным выгоранием. Исследование сервисов HeadHunter и “Доктор рядом” за 2020 год показало, что половина из 2,5 тысяч опрошенных работников испытывают тревогу, чуть меньше опрошенных (48%) из-за переутомления стали эмоционально бесчувственными, работают на автомате и ощущают опустошение при выполнении задач. 45% респондентов испытывают личностное отчуждение по отношению к коллегам.
Если вы тоже замечаете за собой такое состояние или его зачатки, то вот Х советов, которые помогут вам справиться с выгоранием и увеличить продуктивность без смены работы и психотерапевта:
Заботьтесь о своем здоровье. 
Сбалансированно питайтесь, наладьте режим сна, занимайтесь спортом, гуляйте на свежем воздухе и полноценно отдыхайте в выходные.
Научитесь отключаться от работы
Многим людям с “синдромом менеджера” сложно найти время на отдых и отвлечься от работы. Но это необходимо, чтобы восстановиться и не растерять мотивацию. Например, в нашем коворкинге Qubity Space есть комната для отдыха с удобными креслами и игровая зона с турником, брусьями, гантелями и скакалкой. Здесь вы не только сделаете перерыв, но и сможете подтянуть свою физическую форму.
Следите за уровнем стресса
Даже если вам кажется, что стресс - неотъемлимая часть вашей жизни и от него нельзя избавиться, то вы ошибаетесь. Значительно уменьшить его влияние помогут рефлексия, медитация, дыхательные практики, а также смена обстановки. 
Поговорите с тем, кому вы доверяете
Это может быть друг, партнер, родители, коллега. Общение с приятными людьми помогает нам расслабиться, поделиться своими чувствами и эмоциями. В нашем коворкинге вы можете работать вместе с коллегами, а также найти новые знакомства среди сильных специалистов в вашей сфере, которые в будущем могут стать вашими друзьями или партнерами.
Сохраняйте свои личные границы
Если игнорировать собственные эмоции и позволять их постоянно нарушать, то рано или поздно вы сталкнетесь с симптомами выгорания. Чтобы такого не произошло, научитесь говорить нет, сократите контакты с неприятными людьми, уберите все раздражители, особенно на работе. Выбирая для работы офис в коворкинге Qubity Space, вы будете находиться в изолированном пространстве, где вас не будут отвлекать и тревожить, чтобы вы могли сосредоточиться на своих задачах без чужого вмешательства.
Планируйте отдых
Очень сложно расслабиться, когда 24/7 думаете о работе. Поэтому важно выделять в своём расписании перерывы на отдых. Например, в нашем пространстве есть оборудованная кухня с кофемашиной, куда вы можете отойти, чтобы сделать вкусный кофе и перекусить фруктами и полезными снеками и еще быстрее восстановить силы. 
Обустройте рабочее место. 
Для продуктивной работы (и здоровой спины) нужен удобный стол и стул, достаточно света и свежего воздуха. В наших офисах настроена система вентиляции, большие окна и много света, чтобы вы могли чувствовать себя хорошо ментально и физически.

Эти простые советы помогут  не только справиться с симптомами эмоцианального выгорания, но и приобрести полезные привычки для вашей повседневной жизни.

Ощутимо повысить продуктивность за 1 день вы сможете на бесплатном посещении нашего коворкинга Qubity Space.
В следующих сообщениях Вы получите больше информации о нашем коворинге.''')
                await asyncio.sleep(86400)
                await message.answer('''Ошибки коворкингов, которые учтены в Qubity Space

Удаленная работа из дома. В 2020 году все люди принудительно узнали, что это такое и ощутили на себе все плюсы и минусы remote work. И если по началу большинству людей нравилась работать дома,  то со временем они начали уставать от однообразия и монотонности. 
Неплохим решением для многих стали коворкинги – центры, в которых арендовать рабочее место может любой желающий.
Бизнесмены, стартаперы, фрилансеры и просто творческие люди поначалу оценили все плюсы работы в таком месте, но в какой-то момент резиденты подобных заведений понимают, что помещения перестают быть друзьями для их бизнеса. И вот почему:
Трудности при проведении встреч
Open-space не самое подходящее место для встречи с партнерами и клиентами. Согласитесь, не очень хочется, чтобы вокруг тебя находились “лишние уши”. Вашему приглашенному может быть неловко, к тому же, большинство считает такой формат встреч непрестижным.
Резиденты коворкинга Qubity Space могут бесплатно воспользоваться оборудованной переговорной с шумоизоляцией, где точно никто не подслушает и не будет мешать. Если у вас несколько встреч подряд и на предыдущей вы задержались или клиент приехал раньше, то наши приветливые администраторы встретят вашего гостя, проводят его в комнату отдыха, где он сможет комфортно подождать.
Шумный open-space
Посетители большинства коворкингов страдают от шума и невозможности сосредоточиться, когда вокруг много людей. 
В нашем пространстве действует система штрафов - если резидент ведет себя шумно и мешает остальным, администратор сделает ему замечание. За 3 замечания резидент попадает в черный список и не имеет права посещать коворкинг 1 месяц.
Нет гарантии безопасности
Посетить коворкинг может любой человек, который заплатил за аренду места.  Но поскольку на этих площадях часто обитают люди с улицы, степень безопасности личных вещей и идей сокращается. 
В Qubity Space каждый резидент имеет собственный локер, может зайти только по карте-ключу и Face ID, все пространство оборудовано камерами, а за порядком следят администраторы.
Несовпадение графиков
Многие коворкинги уже перешли на круглосуточный режим работы, но еще не везде вы можете поработать в любые часы, и приходится подстраиваться.
Если вы арендуете закрепленное место у нас, то вы можете прийти поработать в любое время суток, даже ночью.
Платная техника, кофе, снеки
Коворкинг - место для работы, отдохнуть и поесть можно дома, или, на крайний случай, в ближайшем кафе.
Мы там не считаем - резиденты Qubity Space вместе с удобным рабочим местом получают еще и неограниченный кофе, фрукты и снеки, бесплатно могут пользоваться любой офисной техникой.

В Qubity Space мы пострались развеять все мифы о работе в коворкингах и сделать пространство максимально комфортным для вашей продуктивности. Будем рады видеть вас в числе наших резидентов!''')
                await asyncio.sleep(86400)
                await message.answer('''Дизайнерский ремонт в современном стиле, панорамные окна, собственный спортзал и кухня - видеообзор пространства Qubity Space

Неважно, успели вы посетить наш коворкинг или еще нет, вы можете посмотреть, как выглядит наше пространство внутри в небольшом видео.
Будучи резидентом, вы сможете посещать все эти зоны и использовать все преимущества коворкинга.
Приятного просмотра!''')
                await asyncio.sleep(86400)
                await message.answer('''Почему работая в коворкинге ты намного быстрее станешь лучше как специалист и начнешь больше зарабатывать? - отзыв от резидента Qubity Space

Меня зовут Дмитрий, я занимаюсь созданием сайтов уже более 8 лет, 5 лет из которых я работаю на фрилансе. Изначально, когда ушел из офиса, работал дома или в кофейне неподалеку. Понял, что работа из дома дается мне нелегко - не могу сосредоточиться, а в кофейне шумно и не всегда есть место, где можно сесть.
Поэтому стал искать коворкинг в Москве, чтобы было удобно и недалеко от меня.
За пару лет поменял несколько мест, где-то нравилось больше, где-то меньше, но везде были свои недостатки. Для работы мне важна тишина, удобное рабочее место и круглосуточный доступ, т.к. иногда люблю зависнуть над проектом до 12 ночи. В большинстве коворкингов этого не хватало.
Пару месяцев назад друг посоветовал посетить коворкинг Qubity Space. Подкупило, что он находится недалеко от моего дома (15 минут пешком). Пришел на тестовый день и уже работаю там с июня. Это потрясающее место. Если судить по внешним факторам — это пожалуй лучшее место, что я встречал. Сразу как попадаешь сюда, интерьер очень подкупает. Внутри все очень красиво и аккуратно. Отличные удобные офисные кресла и столы. Еще мне особенно нравится то, что коворкинг расположен в бизнес-центре в окружении разных заведений и с развитой инфраструктурой. Есть большой выбор, куда сходить на обед. К тому же можно перекусить прямо в самом коворкинге - тут есть большая просторная кухня с бесплатным кофе. 
Что еще поразило - это абсолютная тишина, почти как в библиотеке. Штрафы за шум, конечно, жестко, зато дисциплина отличная. 
Здесь есть удобная выделенная переговорная с проектором, чего я не встречал в остальных коворкингах.
Еще огромный плюс в пользу Qubity Space - можно работать круглосуточно, если арендовать закрепленное место или офис. Никто в 20:00 не выгоняет, как было на моем предыдущем опыте.
Еще один момент, нельзя снимать коворкинг посуточно или на неделю. Только на месяц, по словам администраторов, этим ограничением они хотят избежать текучки людей и создать дружественную среду, где люди между собой знакомы. Что ж, цель хорошая.

В общем, это отличное место для работы, особенно если вы устали от “домашнего офиса”. Обстановка настраивает на рабочий лад.''')
                await asyncio.sleep(86400*3)
                media = types.MediaGroup()
                media.attach_photo("https://i.imgur.com/d2JHzX7.jpg")
                media.attach_photo("https://i.imgur.com/C1Nue4Q.jpg")
                media.attach_photo("https://i.imgur.com/9Zkuyo5.jpg", '''От чего зависит успех деловой встречи?Конечно же от обстановки!

Естественно важны и другие факторы, например, ваша подготовка, внешний вид, умение презентовать и договариваться. Но даже это все не поможет, если проводить переговоры в неподходящем месте.
Это мы учли в наших переговорных комнатах, ведь именно по обстановке зачастую партнеры или гости судят о солидности мероприятия в целом.

В комнате для переговоров имеется:
проектор
флип-чарт
стабильный быстрый Wi-Fi

🚪Арендуемая площадь - 18 кв.м.

🎎Зал вмещает до 10 человек, мебель стоит по принципу «Круглый стол», также по запросу возможна «театральная» расстановка кресел.

☕️Для комфортного проведения деловых мероприятий у вас будет неограниченный доступ к напиткам, фруктам и снекам. Также в перерыве вы можете разместиться в удобной конмнате отдыха и передохнуть.

Каждый резидент с закрепленным рабочим местом получает доступ к переговорной совершенно бесплатно и может забранировать ее от 1 ч в день.''')
                await message.bot.send_media_group(message.chat.id, media=media)
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Какое время работы локаций и есть ли парковка - ответили на самые популярные вопросы о коворкинге Qubity Space 

Можно ли приводить гостей, если у меня самого тестовый день? А прийти на него второй раз в другую локацию?
Пробный день в коворкинге создан для того, чтобы вы могли прочувствовать атмосферу работы в Qubity Space. Если вы уже побывали в одной из локаций и хотите поработать в течение дня в другой, обратите внимание на тариф “Гость”. Если вам необходимо провести встречу, рекомендуем рассмотреть возможность аренды переговорных комнат или также воспользоваться тарифом “Гость”, включающим посещение 1 гостя.
Где можно припарковаться? 
В Qubity Space обратите внимание на подземную парковку или наземную парковку БЦ “Нео Гео”. Позвоните администратору коворкинга заранее, чтобы узнать, доступно ли парковочное место в запланированное вами время посещения коворкинга. Также на срок от 1 месяца возможно арендовать парковочное место в БЦ.
У вас в офисах есть мебель? Можно ли привезти свою? 
Каждый офис Qubity Space оборудован столами и креслами в соответствии с количеством рабочих мест в нем. Обустроить кабинет вы можете на своё усмотрение (только не забудьте предварительно оповестить администратора, если вы собираетесь вносить в коворкинг что-то крупногабаритное). Если мы получаем от резидентов большое количество запросов на какой-то определённый тип мебели (например, тумбы), рассматриваем возможность дополнить обустройство рабочих мест. Также мы предоставляем в аренду персональные локеры.
Время работы локаций? 
Для резидентов, выбравших тариф "Резидент" или Smart-офис коворкинг открыт круглосуточно. Для резидентов коворкинга, выбравших тариф “Гость”, – с 8:00 до 20:00, в рабочее время команды локации.
Как осуществляется охрана коворкинга? 
Вход в коворкинг осуществляется строго по пропускам резидентов и Face-ID. Также в офисных пространствах установлены камеры видеонаблюдения, к записям с которых в случае необходимости мы можем обратиться. Каждый резидент получает собственный локер для хранения личных вещей, а за порядком следят администраторы.
Вы предоставляете юридический адрес?
Юридический адрес является дополнительной услугой и предоставляется только арендаторам кабинетов, выбравшим срок аренды от 11 месяцев, а также арендой от 25 мест. Вначале мы заключаем с вами договор субаренды, затем вы оплачиваете услугу, и мы готовим подтверждающие вашу работу в офисном пространстве документы для налоговой.
Как организовать мероприятие на вашей площадке? 
Если вы уже определились с датой, ознакомьтесь со свободными временными окнами у администраторов пространства. Если дата свободна, можно приступать к обсуждению деталей события: какое техническое оснащение для него потребуются, какой формат рассадки предполагается, какое количество гостей вы ожидаете увидеть. Во всех наших локациях действует пропускная система, поэтому не забудьте при регистрации запросить у гостей их полные ФИО.

Если у вас остались вопросы, то вы можете задать их администраторам коворкинга Qubity, написав боту в ответ на это сообщение или по телефону: +7 (926) 911-13-96.''')
                q = await User.question.set()
                await asyncio.sleep(86400*3)
                if not q:
                    await message.answer('''Что можно купить за 450 Р? 2 чашки кофе или 1 день в современном коворкинге Qubity Space и пить кофе в неограниченном количестве

Стоимость размещения в коворкинге зависит от того, арендуете вы незакрепленное место в open space или закрепленное в офисе, а также от времени доступа в коворкинг. 

Наши тарифы:

Гость - 1000 Р/день
Незакрепленное место в openspace
Доступ 1 день (8:00-20:00)
Кофе-брейки
Лаундж-зона (30 мин.)
Skype-room (30 мин.)
Все общие зоны

Резидент Light - 14.500 Р/месяц
Незакрепленное место в openspace
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Резидент Platinum - 18.500 Р/месяц
Закрепленное место в Smart-офисе
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Smart-офис - от 16.000 Р/чел
Индивидуальный Smart-офис
Доступ 24/7
Кофе-брейки
Лаундж-зона (от 1 ч./день)
Skype-room (от 1 ч./день)
Все общие зоны

Приходите на бесплатный день в коворкинге Qubity Space, чтобы подобрать тариф для себя
Переходите по ссылке на наш сайт, чтобы забронировать бесплатное место в коворкинге: http://qubity.space/''')
                    await state.finish()
            
        else:
            await message.reply(f'Номер телефона состоит из 9-12 чисел. \nОтправьте мне свой номер телефона заново: ')
            await User.number3.set()   
    else:
        await message.reply(f'Отправьте мне свой номер телефона без плюса(+): ')
        await User.number3.set()


@dp.message_handler(state=User.question, content_types='text')
async def get_question(message: types.Message, state: FSMContext):
    if message.text.endswith("?"):
        async with aiosqlite.connect("dbase.db") as con:
            conn = await con.cursor()
            num = await conn.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            num = await num.fetchone()
        m = await message.answer("Отправляю Ваш вопрос менеджеру...")
        await bot.send_message(admin_id, f"<b>Вопрос от <a href='tg://openmessage?user_id={message.from_user.id}'>пользователя</a></b> \nНомер: <code>{num}</code> \n\nВопрос: <code>{message.text}</code>")
        await asyncio.sleep(2.5)
        await bot.edit_message_text(chat_id=message.chat.id, message_id=m.message_id, text="Ваш вопрос успешно доставлен менеджеру. Менеджер скоро свяжется с вами.")
    else:
        await message.reply("Задайте вопрос с вопросительным знаком(?) \nНапример: <i>Как Я могу связаться с менеджером</i><b><u>?</u></b> \n\nВведите Ваш вопрос заново: ")
        q2 = await User.question.set()
        await asyncio.sleep(300)
        if not q2:
            await message.answer("Я отменил ваш запрос на вопрос менеджеру, из-за того что Вы не ввели свой вопрос в течение 5 минут.")
            await state.finish()
            

@dp.message_handler(state=User.number, content_types='text')
async def get_numbers(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        if 12 >= len(list(message.text)) >= 10:
            async with aiosqlite.connect("dbase.db") as con:
                conn = await con.cursor()
                #ans2 = await conn.execute("SELECT a2 FROM users WHERE id = ?;", (message.from_user.id, ))
                #ans2 = await ans2.fetchone()
                #beh[6] = str(ans2)
                await conn.execute('UPDATE users SET number = ? WHERE id = ?', (str(f'{message.text}'), message.from_user.id, ))
                await con.commit()
                info = await conn.execute('SELECT * FROM users WHERE id = ?', (message.from_user.id, ))
                info = await info.fetchall()
            number = await state.update_data(number=message.text)
            beh = str(info[0]).replace("(", "").replace(")", "").replace("'", "").split(", ")
            #if not beh[6] == "Open Space":
            #    await message.answer(f"{type(beh[6])}")
            await state.finish()
            await bot.send_message(chat_id=admin_id, text=f'<b>Время записан в часовом поясе Екатеринбурга(+5)!</b> \nИмя: <code>{message.from_user.first_name}</code> \nФамилия: <code>{message.from_user.last_name}</code> \nНомер: <code>{beh[2]}</code> \nID пользователя: <code>{message.from_user.id}</code> \nЮзернэйм пользователя: <code>@{message.from_user.username}</code> \n\nИнформация о действиях пользователя: \n - Ответ на первый опрос: <b>{beh[3]}</b> \n - Время ответа на первый опрос: <b>{beh[4]} | {beh[5]}</b> \n\n - Ответ на второй опрос: <b>{beh[6]}</b> \n - Время ответа на второй опрос: <b>{beh[7]} | {beh[8]}</b> \n\n - Ответ на третий опрос: <b>{beh[9]}</b> \n - Время ответа на третий опрос: <b>{beh[10]} | {beh[11]}</b> \n\n\n<a href="tg://openmessage?user_id={message.from_user.id}">Перейти к пользователю</a>'.replace("@None", "Отсутствует"), disable_notification=True)
            if beh[6] == "Open Space":
                await message.answer('''Спасибо, мы приняли Ваши контактные данные и забронировали 1 бесплатный день за Вашим номером телефона. 

Что Вас ждет на тестовом дне в коворкинге Qubity Space:
 - 612 м2 пространства для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении
 - удобное рабочее место в тихом open-space для максимально комфортной работы
 - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1 ч)
 - пользование Skype-кабиной для созвонов с шумопоглощением (до 1 ч)
 - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном
 - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой
А еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный Wi-fi

Совсем скоро с вами свяжется Ваш менеджер, уточнит детали вашего визита и ответит на ваши вопросы.

В следующем сообщении Вы получите обещанный бонус: чек-лист для повышения продуктивности работы в офисе''')
                await asyncio.sleep(28800)
                await message.answer('''15 идей как фрилансеру разнообразить свои рабочие будни, чтобы 24/7 не сидеть дома

“Что бы мне поделать, только бы не поработать?”
Если работая дома вы не можете сосредоточиться и постоянно откладываете задачи на потом, вот 15 советов, которые помогут вам оставаться продуктивным на фрилансе и не сойти с ума:
Планируйте завтрашний день
Составляйте с вечера список дел на завтра.  Зная свои приоритеты, вы не станете тратить время на ерунду и будете меньше отвлекаться.
Научитесь отключаться от работы
Очень сложно перестать думать о работе, когда дом и офис — одно и то же место. Но это необходимо, чтобы восстановиться и не растерять мотивацию. Например, в нашем коворкинге Qubity Space есть комната для отдыха с удобными креслами и игровая зона с турником, брусьями, гантелями и скакалкой. Здесь вы не только сделаете перерыв, но и сможете подтянуть свою физическую форму.
Работайте в определённой одежде
Да, это работает! Многие психологи считают, что как и атмосфера вокруг, одежда может создавать ощущение того, что вы на работе. 
Не заходите в соц. сети
Полезно поддерживать профессиональные аккаунты в актуальном состоянии. Но иногда это превращается в бездумный серфинг в интернете и растягивается на несколько часов.
Отчитывайтесь кому-то о дедлайнах
Например, договоритесь с другом или коллегой, что будете оповещать о выполнении какой-то задачи. Стыдно будет признаваться, что вы прокрастинировали и просрочили дедлайн, поэтому вы начнёте больше стараться. В наш коворкинг вы можете приходить с друзьями и даже не придется звонить или писать - вы можете показать результат вживую и спросить совета, если в чем-то неуверены.
Всегда имейте в запасе какую-то механическую работу
Иногда просто нет сил на сложные задачи, требующие творческого подхода или концентрации. На такие случаи составьте список необходимых, но скучных механических дел.
Планируйте отдых
Очень сложно расслабиться, когда рабочее место прямо под боком. Поэтому важно выделять в своём расписании перерывы на отдых. Например, в нашем пространстве есть оборудованная кухня с кофемашиной, куда вы можете отойти, чтобы сделать вкусный кофе и перекусить фруктами и полезными снеками и еще быстрее восстановить силы. 
Не отвлекайтесь
Когда вы находитемь дома, где за вами никто не следит, у вас может возникать желание отвлечься на что-то или на кого-то. И так вы не заметите, как пройдет час или два. В коворкинге Qubity Space вы будете находится в окружении работающих людей, глядя на которых вам не захочется прокрастинировать. А еще там нет домашних дел, а уборку выполняет клининг.
Обустройте рабочее место. 
Для продуктивной работы (и здоровой спины) нужен удобный стол и стул, достаточно света и свежего воздуха. Работать лежа в кровати, конечно, приятно, но до момента пока вас не будет постоянно клонить в сон. В нашем open-space вы можете разместиться как за столом на мягком кресле, так и на мягком диване и кресле мешке. А смена обстановки будет позитивно влиять на вашу бодрость и настроение.
Постоянно общайтесь с людьми
Личное общение трудно переоценить, даже если вы интроверт. Оно даёт новые идеи и просто помогает выбраться из собственного пузыря. В нашем бизнес-коворкинге может одновременно работать до 112 человек - среди них вы точно найдете единомышленника, а, возможно, и будущего друга или партнера.

Эти простые советы помогут  не только справляться с работой проще и быстрее, но и приобрести полезные привычки для вашей повседневной жизни.

Ощутимо повысить продуктивность за 1 день вы сможете на бесплатном посещении нашего коворкинга Qubity Space.

В следующих сообщениях Вы получите больше информации о нашем коворинге.''')
                await asyncio.sleep(86400)
                await message.answer('''Ошибки коворкингов, которые учтены в Qubity Space

Удаленная работа из дома. В 2020 году все люди принудительно узнали, что это такое и ощутили на себе все плюсы и минусы remote work. И если по началу большинству людей нравилась работать дома,  то со временем они начали уставать от однообразия и монотонности. 
Неплохим решением для многих стали коворкинги – центры, в которых арендовать рабочее место может любой желающий.
Бизнесмены, стартаперы, фрилансеры и просто творческие люди поначалу оценили все плюсы работы в таком месте, но в какой-то момент резиденты подобных заведений понимают, что помещения перестают быть друзьями для их бизнеса. И вот почему:
Трудности при проведении встреч
Open-space не самое подходящее место для встречи с партнерами и клиентами. Согласитесь, не очень хочется, чтобы вокруг тебя находились “лишние уши”. Вашему приглашенному может быть неловко, к тому же, большинство считает такой формат встреч непрестижным.
Резиденты коворкинга Qubity Space могут бесплатно воспользоваться оборудованной переговорной с шумоизоляцией, где точно никто не подслушает и не будет мешать. Если у вас несколько встреч подряд и на предыдущей вы задержались или клиент приехал раньше, то наши приветливые администраторы встретят вашего гостя, проводят его в комнату отдыха, где он сможет комфортно подождать.
Шумный open-space
Посетители большинства коворкингов страдают от шума и невозможности сосредоточиться, когда вокруг много людей. 
В нашем пространстве действует система штрафов - если резидент ведет себя шумно и мешает остальным, администратор сделает ему замечание. За 3 замечания резидент попадает в черный список и не имеет права посещать коворкинг 1 месяц.
Нет гарантии безопасности
Посетить коворкинг может любой человек, который заплатил за аренду места.  Но поскольку на этих площадях часто обитают люди с улицы, степень безопасности личных вещей и идей сокращается. 
В Qubity Space каждый резидент имеет собственный локер, может зайти только по карте-ключу и Face ID, все пространство оборудовано камерами, а за порядком следят администраторы.
Несовпадение графиков
Многие коворкинги уже перешли на круглосуточный режим работы, но еще не везде вы можете поработать в любые часы, и приходится подстраиваться.
Если вы арендуете закрепленное место у нас, то вы можете прийти поработать в любое время суток, даже ночью.
Платная техника, кофе, снеки
Коворкинг - место для работы, отдохнуть и поесть можно дома, или, на крайний случай, в ближайшем кафе.
Мы там не считаем - резиденты Qubity Space вместе с удобным рабочим местом получают еще и неограниченный кофе, фрукты и снеки, бесплатно могут пользоваться любой офисной техникой.

В Qubity Space мы пострались развеять все мифы о работе в коворкингах и сделать пространство максимально комфортным для вашей продуктивности. Будем рады видеть вас в числе наших резидентов!''')
                await asyncio.sleep(86400)
                await message.answer('''Дизайнерский ремонт в современном стиле, панорамные окна, собственный спортзал и кухня - видеообзор пространства Qubity Space

Неважно, успели вы посетить наш коворкинг или еще нет, вы можете посмотреть, как выглядит наше пространство внутри в небольшом видео.
Будучи резидентом, вы сможете посещать все эти зоны и использовать все преимущества коворкинга.
Приятного просмотра!''')
                await asyncio.sleep(86400)
                await message.answer('''Почему работая в коворкинге ты намного быстрее станешь лучше как специалист и начнешь больше зарабатывать? - отзыв от резидента Qubity Space

Меня зовут Дмитрий, я занимаюсь созданием сайтов уже более 8 лет, 5 лет из которых я работаю на фрилансе. Изначально, когда ушел из офиса, работал дома или в кофейне неподалеку. Понял, что работа из дома дается мне нелегко - не могу сосредоточиться, а в кофейне шумно и не всегда есть место, где можно сесть.
Поэтому стал искать коворкинг в Москве, чтобы было удобно и недалеко от меня.
За пару лет поменял несколько мест, где-то нравилось больше, где-то меньше, но везде были свои недостатки. Для работы мне важна тишина, удобное рабочее место и круглосуточный доступ, т.к. иногда люблю зависнуть над проектом до 12 ночи. В большинстве коворкингов этого не хватало.
Пару месяцев назад друг посоветовал посетить коворкинг Qubity Space. Подкупило, что он находится недалеко от моего дома (15 минут пешком). Пришел на тестовый день и уже работаю там с июня. Это потрясающее место. Если судить по внешним факторам — это пожалуй лучшее место, что я встречал. Сразу как попадаешь сюда, интерьер очень подкупает. Внутри все очень красиво и аккуратно. Отличные удобные офисные кресла и столы. Еще мне особенно нравится то, что коворкинг расположен в бизнес-центре в окружении разных заведений и с развитой инфраструктурой. Есть большой выбор, куда сходить на обед. К тому же можно перекусить прямо в самом коворкинге - тут есть большая просторная кухня с бесплатным кофе. 
Что еще поразило - это абсолютная тишина, почти как в библиотеке. Штрафы за шум, конечно, жестко, зато дисциплина отличная. 
Здесь есть удобная выделенная переговорная с проектором, чего я не встречал в остальных коворкингах.
Еще огромный плюс в пользу Qubity Space - можно работать круглосуточно, если арендовать закрепленное место или офис. Никто в 20:00 не выгоняет, как было на моем предыдущем опыте.
Еще один момент, нельзя снимать коворкинг посуточно или на неделю. Только на месяц, по словам администраторов, этим ограничением они хотят избежать текучки людей и создать дружественную среду, где люди между собой знакомы. Что ж, цель хорошая.

В общем, это отличное место для работы, особенно если вы устали от “домашнего офиса”. Обстановка настраивает на рабочий лад.''')
                await asyncio.sleep(86400*3)
                media = types.MediaGroup()
                media.attach_photo("https://i.imgur.com/d2JHzX7.jpg")
                media.attach_photo("https://i.imgur.com/C1Nue4Q.jpg")
                media.attach_photo("https://i.imgur.com/9Zkuyo5.jpg", '''От чего зависит успех деловой встречи?Конечно же от обстановки!

Естественно важны и другие факторы, например, ваша подготовка, внешний вид, умение презентовать и договариваться. Но даже это все не поможет, если проводить переговоры в неподходящем месте.
Это мы учли в наших переговорных комнатах, ведь именно по обстановке зачастую партнеры или гости судят о солидности мероприятия в целом.

В комнате для переговоров имеется:
проектор
флип-чарт
стабильный быстрый Wi-Fi

🚪Арендуемая площадь - 18 кв.м.

🎎Зал вмещает до 10 человек, мебель стоит по принципу «Круглый стол», также по запросу возможна «театральная» расстановка кресел.

☕️Для комфортного проведения деловых мероприятий у вас будет неограниченный доступ к напиткам, фруктам и снекам. Также в перерыве вы можете разместиться в удобной конмнате отдыха и передохнуть.

Каждый резидент с закрепленным рабочим местом получает доступ к переговорной совершенно бесплатно и может забранировать ее от 1 ч в день.''')
                await message.bot.send_media_group(message.chat.id, media=media)
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Какое время работы локаций и есть ли парковка - ответили на самые популярные вопросы о коворкинге Qubity Space 

Можно ли приводить гостей, если у меня самого тестовый день? А прийти на него второй раз в другую локацию?
Пробный день в коворкинге создан для того, чтобы вы могли прочувствовать атмосферу работы в Qubity Space. Если вы уже побывали в одной из локаций и хотите поработать в течение дня в другой, обратите внимание на тариф “Гость”. Если вам необходимо провести встречу, рекомендуем рассмотреть возможность аренды переговорных комнат или также воспользоваться тарифом “Гость”, включающим посещение 1 гостя.
Где можно припарковаться? 
В Qubity Space обратите внимание на подземную парковку или наземную парковку БЦ “Нео Гео”. Позвоните администратору коворкинга заранее, чтобы узнать, доступно ли парковочное место в запланированное вами время посещения коворкинга. Также на срок от 1 месяца возможно арендовать парковочное место в БЦ.
У вас в офисах есть мебель? Можно ли привезти свою? 
Каждый офис Qubity Space оборудован столами и креслами в соответствии с количеством рабочих мест в нем. Обустроить кабинет вы можете на своё усмотрение (только не забудьте предварительно оповестить администратора, если вы собираетесь вносить в коворкинг что-то крупногабаритное). Если мы получаем от резидентов большое количество запросов на какой-то определённый тип мебели (например, тумбы), рассматриваем возможность дополнить обустройство рабочих мест. Также мы предоставляем в аренду персональные локеры.
Время работы локаций? 
Для резидентов, выбравших тариф "Резидент" или Smart-офис коворкинг открыт круглосуточно. Для резидентов коворкинга, выбравших тариф “Гость”, – с 8:00 до 20:00, в рабочее время команды локации.
Как осуществляется охрана коворкинга? 
Вход в коворкинг осуществляется строго по пропускам резидентов и Face-ID. Также в офисных пространствах установлены камеры видеонаблюдения, к записям с которых в случае необходимости мы можем обратиться. Каждый резидент получает собственный локер для хранения личных вещей, а за порядком следят администраторы.
Вы предоставляете юридический адрес?
Юридический адрес является дополнительной услугой и предоставляется только арендаторам кабинетов, выбравшим срок аренды от 11 месяцев, а также арендой от 25 мест. Вначале мы заключаем с вами договор субаренды, затем вы оплачиваете услугу, и мы готовим подтверждающие вашу работу в офисном пространстве документы для налоговой.
Как организовать мероприятие на вашей площадке? 
Если вы уже определились с датой, ознакомьтесь со свободными временными окнами у администраторов пространства. Если дата свободна, можно приступать к обсуждению деталей события: какое техническое оснащение для него потребуются, какой формат рассадки предполагается, какое количество гостей вы ожидаете увидеть. Во всех наших локациях действует пропускная система, поэтому не забудьте при регистрации запросить у гостей их полные ФИО.

Если у вас остались вопросы, то вы можете задать их администраторам коворкинга Qubity, написав боту в ответ на это сообщение или по телефону: +7 (926) 911-13-96.''')
                q = await User.question.set()
                await asyncio.sleep(86400*3)
                if not q:
                    await message.answer('''Что можно купить за 450 Р? 2 чашки кофе или 1 день в современном коворкинге Qubity Space и пить кофе в неограниченном количестве

Стоимость размещения в коворкинге зависит от того, арендуете вы незакрепленное место в open space или закрепленное в офисе, а также от времени доступа в коворкинг. 

Наши тарифы:

Гость - 1000 Р/день
Незакрепленное место в openspace
Доступ 1 день (8:00-20:00)
Кофе-брейки
Лаундж-зона (30 мин.)
Skype-room (30 мин.)
Все общие зоны

Резидент Light - 14.500 Р/месяц
Незакрепленное место в openspace
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Резидент Platinum - 18.500 Р/месяц
Закрепленное место в Smart-офисе
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Smart-офис - от 16.000 Р/чел
Индивидуальный Smart-офис
Доступ 24/7
Кофе-брейки
Лаундж-зона (от 1 ч./день)
Skype-room (от 1 ч./день)
Все общие зоны

Приходите на бесплатный день в коворкинге Qubity Space, чтобы подобрать тариф для себя
Переходите по ссылке на наш сайт, чтобы забронировать бесплатное место в коворкинге: http://qubity.space/''')
                    await state.finish()
            elif beh[6] == "Офис на сутки":
                await message.answer('''Спасибо, мы приняли Ваши контактные данные и забронировали 1 бесплатный день за Вашим номером телефона. 

Что Вас ждет на тестовом дне в коворкинге Qubity Space:
 - 612 м2 пространства для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении
 - удобное рабочее место в тихом open-space для максимально комфортной работы
 - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1 ч)
 - пользование Skype-кабиной для созвонов с шумопоглощением (до 1 ч)
 - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном
 - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой
А еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный Wi-fi

Совсем скоро с вами свяжется Ваш менеджер, уточнит детали вашего визита и ответит на ваши вопросы.

В следующем сообщении Вы получите обещанный бонус: чек-лист для повышения продуктивности работы в офисе''')
                await asyncio.sleep(28800)
                await message.answer('''Как рабочая обстановка помогает бороться с эмоциональным выгоранием и увеличивает продуктивность

Последние тенденции общества направлены на поддержание не только физического, но и ментального здоровья. Так как работа занимает большую часть нашей повседневной жизни, специалисты все чаще жалуются на стресс, хроническую усталость и раздражительность. Психологи называют такое состояние эмоциональным выгоранием. Исследование сервисов HeadHunter и “Доктор рядом” за 2020 год показало, что половина из 2,5 тысяч опрошенных работников испытывают тревогу, чуть меньше опрошенных (48%) из-за переутомления стали эмоционально бесчувственными, работают на автомате и ощущают опустошение при выполнении задач. 45% респондентов испытывают личностное отчуждение по отношению к коллегам.
Если вы тоже замечаете за собой такое состояние или его зачатки, то вот Х советов, которые помогут вам справиться с выгоранием и увеличить продуктивность без смены работы и психотерапевта:
Заботьтесь о своем здоровье. 
Сбалансированно питайтесь, наладьте режим сна, занимайтесь спортом, гуляйте на свежем воздухе и полноценно отдыхайте в выходные.
Научитесь отключаться от работы
Многим людям с “синдромом менеджера” сложно найти время на отдых и отвлечься от работы. Но это необходимо, чтобы восстановиться и не растерять мотивацию. Например, в нашем коворкинге Qubity Space есть комната для отдыха с удобными креслами и игровая зона с турником, брусьями, гантелями и скакалкой. Здесь вы не только сделаете перерыв, но и сможете подтянуть свою физическую форму.
Следите за уровнем стресса
Даже если вам кажется, что стресс - неотъемлимая часть вашей жизни и от него нельзя избавиться, то вы ошибаетесь. Значительно уменьшить его влияние помогут рефлексия, медитация, дыхательные практики, а также смена обстановки. 
Поговорите с тем, кому вы доверяете
Это может быть друг, партнер, родители, коллега. Общение с приятными людьми помогает нам расслабиться, поделиться своими чувствами и эмоциями. В нашем коворкинге вы можете работать вместе с коллегами, а также найти новые знакомства среди сильных специалистов в вашей сфере, которые в будущем могут стать вашими друзьями или партнерами.
Сохраняйте свои личные границы
Если игнорировать собственные эмоции и позволять их постоянно нарушать, то рано или поздно вы сталкнетесь с симптомами выгорания. Чтобы такого не произошло, научитесь говорить нет, сократите контакты с неприятными людьми, уберите все раздражители, особенно на работе. Выбирая для работы офис в коворкинге Qubity Space, вы будете находиться в изолированном пространстве, где вас не будут отвлекать и тревожить, чтобы вы могли сосредоточиться на своих задачах без чужого вмешательства.
Планируйте отдых
Очень сложно расслабиться, когда 24/7 думаете о работе. Поэтому важно выделять в своём расписании перерывы на отдых. Например, в нашем пространстве есть оборудованная кухня с кофемашиной, куда вы можете отойти, чтобы сделать вкусный кофе и перекусить фруктами и полезными снеками и еще быстрее восстановить силы. 
Обустройте рабочее место. 
Для продуктивной работы (и здоровой спины) нужен удобный стол и стул, достаточно света и свежего воздуха. В наших офисах настроена система вентиляции, большие окна и много света, чтобы вы могли чувствовать себя хорошо ментально и физически.

Эти простые советы помогут  не только справиться с симптомами эмоцианального выгорания, но и приобрести полезные привычки для вашей повседневной жизни.

Ощутимо повысить продуктивность за 1 день вы сможете на бесплатном посещении нашего коворкинга Qubity Space.

В следующих сообщениях Вы получите больше информации о нашем коворинге.''')
                await asyncio.sleep(86400)
                await message.answer('''Ошибки коворкингов, которые учтены в Qubity Space

Удаленная работа из дома. В 2020 году все люди принудительно узнали, что это такое и ощутили на себе все плюсы и минусы remote work. И если по началу большинству людей нравилась работать дома,  то со временем они начали уставать от однообразия и монотонности. 
Неплохим решением для многих стали коворкинги – центры, в которых арендовать рабочее место может любой желающий.
Бизнесмены, стартаперы, фрилансеры и просто творческие люди поначалу оценили все плюсы работы в таком месте, но в какой-то момент резиденты подобных заведений понимают, что помещения перестают быть друзьями для их бизнеса. И вот почему:
Трудности при проведении встреч
Open-space не самое подходящее место для встречи с партнерами и клиентами. Согласитесь, не очень хочется, чтобы вокруг тебя находились “лишние уши”. Вашему приглашенному может быть неловко, к тому же, большинство считает такой формат встреч непрестижным.
Резиденты коворкинга Qubity Space могут бесплатно воспользоваться оборудованной переговорной с шумоизоляцией, где точно никто не подслушает и не будет мешать. Если у вас несколько встреч подряд и на предыдущей вы задержались или клиент приехал раньше, то наши приветливые администраторы встретят вашего гостя, проводят его в комнату отдыха, где он сможет комфортно подождать.
Шумный open-space
Посетители большинства коворкингов страдают от шума и невозможности сосредоточиться, когда вокруг много людей. 
В нашем пространстве действует система штрафов - если резидент ведет себя шумно и мешает остальным, администратор сделает ему замечание. За 3 замечания резидент попадает в черный список и не имеет права посещать коворкинг 1 месяц.
Нет гарантии безопасности
Посетить коворкинг может любой человек, который заплатил за аренду места.  Но поскольку на этих площадях часто обитают люди с улицы, степень безопасности личных вещей и идей сокращается. 
В Qubity Space каждый резидент имеет собственный локер, может зайти только по карте-ключу и Face ID, все пространство оборудовано камерами, а за порядком следят администраторы.
Несовпадение графиков
Многие коворкинги уже перешли на круглосуточный режим работы, но еще не везде вы можете поработать в любые часы, и приходится подстраиваться.
Если вы арендуете закрепленное место у нас, то вы можете прийти поработать в любое время суток, даже ночью.
Платная техника, кофе, снеки
Коворкинг - место для работы, отдохнуть и поесть можно дома, или, на крайний случай, в ближайшем кафе.
Мы там не считаем - резиденты Qubity Space вместе с удобным рабочим местом получают еще и неограниченный кофе, фрукты и снеки, бесплатно могут пользоваться любой офисной техникой.

В Qubity Space мы пострались развеять все мифы о работе в коворкингах и сделать пространство максимально комфортным для вашей продуктивности. Будем рады видеть вас в числе наших резидентов!''')
                await asyncio.sleep(86400)
                await message.answer('''Дизайнерский ремонт в современном стиле, панорамные окна, собственный спортзал и кухня - видеообзор пространства Qubity Space

Неважно, успели вы посетить наш коворкинг или еще нет, вы можете посмотреть, как выглядит наше пространство внутри в небольшом видео.
Будучи резидентом, вы сможете посещать все эти зоны и использовать все преимущества коворкинга.
Приятного просмотра!''')
                await asyncio.sleep(86400)
                await message.answer('''Почему работая в коворкинге ты намного быстрее станешь лучше как специалист и начнешь больше зарабатывать? - отзыв от резидента Qubity Space

Меня зовут Дмитрий, я занимаюсь созданием сайтов уже более 8 лет, 5 лет из которых я работаю на фрилансе. Изначально, когда ушел из офиса, работал дома или в кофейне неподалеку. Понял, что работа из дома дается мне нелегко - не могу сосредоточиться, а в кофейне шумно и не всегда есть место, где можно сесть.
Поэтому стал искать коворкинг в Москве, чтобы было удобно и недалеко от меня.
За пару лет поменял несколько мест, где-то нравилось больше, где-то меньше, но везде были свои недостатки. Для работы мне важна тишина, удобное рабочее место и круглосуточный доступ, т.к. иногда люблю зависнуть над проектом до 12 ночи. В большинстве коворкингов этого не хватало.
Пару месяцев назад друг посоветовал посетить коворкинг Qubity Space. Подкупило, что он находится недалеко от моего дома (15 минут пешком). Пришел на тестовый день и уже работаю там с июня. Это потрясающее место. Если судить по внешним факторам — это пожалуй лучшее место, что я встречал. Сразу как попадаешь сюда, интерьер очень подкупает. Внутри все очень красиво и аккуратно. Отличные удобные офисные кресла и столы. Еще мне особенно нравится то, что коворкинг расположен в бизнес-центре в окружении разных заведений и с развитой инфраструктурой. Есть большой выбор, куда сходить на обед. К тому же можно перекусить прямо в самом коворкинге - тут есть большая просторная кухня с бесплатным кофе. 
Что еще поразило - это абсолютная тишина, почти как в библиотеке. Штрафы за шум, конечно, жестко, зато дисциплина отличная. 
Здесь есть удобная выделенная переговорная с проектором, чего я не встречал в остальных коворкингах.
Еще огромный плюс в пользу Qubity Space - можно работать круглосуточно, если арендовать закрепленное место или офис. Никто в 20:00 не выгоняет, как было на моем предыдущем опыте.
Еще один момент, нельзя снимать коворкинг посуточно или на неделю. Только на месяц, по словам администраторов, этим ограничением они хотят избежать текучки людей и создать дружественную среду, где люди между собой знакомы. Что ж, цель хорошая.

В общем, это отличное место для работы, особенно если вы устали от “домашнего офиса”. Обстановка настраивает на рабочий лад.''')
                await asyncio.sleep(86400*3)
                media = types.MediaGroup()
                media.attach_photo("https://i.imgur.com/d2JHzX7.jpg")
                media.attach_photo("https://i.imgur.com/C1Nue4Q.jpg")
                media.attach_photo("https://i.imgur.com/9Zkuyo5.jpg", '''От чего зависит успех деловой встречи?Конечно же от обстановки!

Естественно важны и другие факторы, например, ваша подготовка, внешний вид, умение презентовать и договариваться. Но даже это все не поможет, если проводить переговоры в неподходящем месте.
Это мы учли в наших переговорных комнатах, ведь именно по обстановке зачастую партнеры или гости судят о солидности мероприятия в целом.

В комнате для переговоров имеется:
проектор
флип-чарт
стабильный быстрый Wi-Fi

🚪Арендуемая площадь - 18 кв.м.

🎎Зал вмещает до 10 человек, мебель стоит по принципу «Круглый стол», также по запросу возможна «театральная» расстановка кресел.

☕️Для комфортного проведения деловых мероприятий у вас будет неограниченный доступ к напиткам, фруктам и снекам. Также в перерыве вы можете разместиться в удобной конмнате отдыха и передохнуть.

Каждый резидент с закрепленным рабочим местом получает доступ к переговорной совершенно бесплатно и может забранировать ее от 1 ч в день.''')
                await message.bot.send_media_group(message.chat.id, media=media)
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Какое время работы локаций и есть ли парковка - ответили на самые популярные вопросы о коворкинге Qubity Space 

Можно ли приводить гостей, если у меня самого тестовый день? А прийти на него второй раз в другую локацию?
Пробный день в коворкинге создан для того, чтобы вы могли прочувствовать атмосферу работы в Qubity Space. Если вы уже побывали в одной из локаций и хотите поработать в течение дня в другой, обратите внимание на тариф “Гость”. Если вам необходимо провести встречу, рекомендуем рассмотреть возможность аренды переговорных комнат или также воспользоваться тарифом “Гость”, включающим посещение 1 гостя.
Где можно припарковаться? 
В Qubity Space обратите внимание на подземную парковку или наземную парковку БЦ “Нео Гео”. Позвоните администратору коворкинга заранее, чтобы узнать, доступно ли парковочное место в запланированное вами время посещения коворкинга. Также на срок от 1 месяца возможно арендовать парковочное место в БЦ.
У вас в офисах есть мебель? Можно ли привезти свою? 
Каждый офис Qubity Space оборудован столами и креслами в соответствии с количеством рабочих мест в нем. Обустроить кабинет вы можете на своё усмотрение (только не забудьте предварительно оповестить администратора, если вы собираетесь вносить в коворкинг что-то крупногабаритное). Если мы получаем от резидентов большое количество запросов на какой-то определённый тип мебели (например, тумбы), рассматриваем возможность дополнить обустройство рабочих мест. Также мы предоставляем в аренду персональные локеры.
Время работы локаций? 
Для резидентов, выбравших тариф "Резидент" или Smart-офис коворкинг открыт круглосуточно. Для резидентов коворкинга, выбравших тариф “Гость”, – с 8:00 до 20:00, в рабочее время команды локации.
Как осуществляется охрана коворкинга? 
Вход в коворкинг осуществляется строго по пропускам резидентов и Face-ID. Также в офисных пространствах установлены камеры видеонаблюдения, к записям с которых в случае необходимости мы можем обратиться. Каждый резидент получает собственный локер для хранения личных вещей, а за порядком следят администраторы.
Вы предоставляете юридический адрес?
Юридический адрес является дополнительной услугой и предоставляется только арендаторам кабинетов, выбравшим срок аренды от 11 месяцев, а также арендой от 25 мест. Вначале мы заключаем с вами договор субаренды, затем вы оплачиваете услугу, и мы готовим подтверждающие вашу работу в офисном пространстве документы для налоговой.
Как организовать мероприятие на вашей площадке? 
Если вы уже определились с датой, ознакомьтесь со свободными временными окнами у администраторов пространства. Если дата свободна, можно приступать к обсуждению деталей события: какое техническое оснащение для него потребуются, какой формат рассадки предполагается, какое количество гостей вы ожидаете увидеть. Во всех наших локациях действует пропускная система, поэтому не забудьте при регистрации запросить у гостей их полные ФИО.

Если у вас остались вопросы, то вы можете задать их администраторам коворкинга Qubity, написав боту в ответ на это сообщение или по телефону: +7 (926) 911-13-96.''')
                q = await User.question.set()
                await asyncio.sleep(86400*3)
                if not q:
                    await message.answer('''Что можно купить за 450 Р? 2 чашки кофе или 1 день в современном коворкинге Qubity Space и пить кофе в неограниченном количестве

Стоимость размещения в коворкинге зависит от того, арендуете вы незакрепленное место в open space или закрепленное в офисе, а также от времени доступа в коворкинг. 

Наши тарифы:

Гость - 1000 Р/день
Незакрепленное место в openspace
Доступ 1 день (8:00-20:00)
Кофе-брейки
Лаундж-зона (30 мин.)
Skype-room (30 мин.)
Все общие зоны

Резидент Light - 14.500 Р/месяц
Незакрепленное место в openspace
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Резидент Platinum - 18.500 Р/месяц
Закрепленное место в Smart-офисе
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Smart-офис - от 16.000 Р/чел
Индивидуальный Smart-офис
Доступ 24/7
Кофе-брейки
Лаундж-зона (от 1 ч./день)
Skype-room (от 1 ч./день)
Все общие зоны

Приходите на бесплатный день в коворкинге Qubity Space, чтобы подобрать тариф для себя
Переходите по ссылке на наш сайт, чтобы забронировать бесплатное место в коворкинге: http://qubity.space/''')
                    await state.finish()
            
            elif beh[6] == "Офис на долгое время":
                await message.answer('''Спасибо, мы приняли Ваши контактные данные и забронировали 1 бесплатный день за Вашим номером телефона. 

Что Вас ждет на тестовом дне в коворкинге Qubity Space:
 - 612 м2 пространства для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении
 - удобное рабочее место в тихом open-space для максимально комфортной работы
 - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1 ч)
 - пользование Skype-кабиной для созвонов с шумопоглощением (до 1 ч)
 - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном
 - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой
А еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный Wi-fi

Совсем скоро с вами свяжется Ваш менеджер, уточнит детали вашего визита и ответит на ваши вопросы.

В следующем сообщении Вы получите обещанный бонус: чек-лист для повышения продуктивности работы в офисе''')
                await asyncio.sleep(28800)
                await message.answer('''Как рабочая обстановка помогает бороться с эмоциональным выгоранием и увеличивает продуктивность

Последние тенденции общества направлены на поддержание не только физического, но и ментального здоровья. Так как работа занимает большую часть нашей повседневной жизни, специалисты все чаще жалуются на стресс, хроническую усталость и раздражительность. Психологи называют такое состояние эмоциональным выгоранием. Исследование сервисов HeadHunter и “Доктор рядом” за 2020 год показало, что половина из 2,5 тысяч опрошенных работников испытывают тревогу, чуть меньше опрошенных (48%) из-за переутомления стали эмоционально бесчувственными, работают на автомате и ощущают опустошение при выполнении задач. 45% респондентов испытывают личностное отчуждение по отношению к коллегам.
Если вы тоже замечаете за собой такое состояние или его зачатки, то вот Х советов, которые помогут вам справиться с выгоранием и увеличить продуктивность без смены работы и психотерапевта:
Заботьтесь о своем здоровье. 
Сбалансированно питайтесь, наладьте режим сна, занимайтесь спортом, гуляйте на свежем воздухе и полноценно отдыхайте в выходные.
Научитесь отключаться от работы
Многим людям с “синдромом менеджера” сложно найти время на отдых и отвлечься от работы. Но это необходимо, чтобы восстановиться и не растерять мотивацию. Например, в нашем коворкинге Qubity Space есть комната для отдыха с удобными креслами и игровая зона с турником, брусьями, гантелями и скакалкой. Здесь вы не только сделаете перерыв, но и сможете подтянуть свою физическую форму.
Следите за уровнем стресса
Даже если вам кажется, что стресс - неотъемлимая часть вашей жизни и от него нельзя избавиться, то вы ошибаетесь. Значительно уменьшить его влияние помогут рефлексия, медитация, дыхательные практики, а также смена обстановки. 
Поговорите с тем, кому вы доверяете
Это может быть друг, партнер, родители, коллега. Общение с приятными людьми помогает нам расслабиться, поделиться своими чувствами и эмоциями. В нашем коворкинге вы можете работать вместе с коллегами, а также найти новые знакомства среди сильных специалистов в вашей сфере, которые в будущем могут стать вашими друзьями или партнерами.
Сохраняйте свои личные границы
Если игнорировать собственные эмоции и позволять их постоянно нарушать, то рано или поздно вы сталкнетесь с симптомами выгорания. Чтобы такого не произошло, научитесь говорить нет, сократите контакты с неприятными людьми, уберите все раздражители, особенно на работе. Выбирая для работы офис в коворкинге Qubity Space, вы будете находиться в изолированном пространстве, где вас не будут отвлекать и тревожить, чтобы вы могли сосредоточиться на своих задачах без чужого вмешательства.
Планируйте отдых
Очень сложно расслабиться, когда 24/7 думаете о работе. Поэтому важно выделять в своём расписании перерывы на отдых. Например, в нашем пространстве есть оборудованная кухня с кофемашиной, куда вы можете отойти, чтобы сделать вкусный кофе и перекусить фруктами и полезными снеками и еще быстрее восстановить силы. 
Обустройте рабочее место. 
Для продуктивной работы (и здоровой спины) нужен удобный стол и стул, достаточно света и свежего воздуха. В наших офисах настроена система вентиляции, большие окна и много света, чтобы вы могли чувствовать себя хорошо ментально и физически.

Эти простые советы помогут  не только справиться с симптомами эмоцианального выгорания, но и приобрести полезные привычки для вашей повседневной жизни.

Ощутимо повысить продуктивность за 1 день вы сможете на бесплатном посещении нашего коворкинга Qubity Space.

В следующих сообщениях Вы получите больше информации о нашем коворинге.''')
                await asyncio.sleep(86400)
                await message.answer('''Ошибки коворкингов, которые учтены в Qubity Space

Удаленная работа из дома. В 2020 году все люди принудительно узнали, что это такое и ощутили на себе все плюсы и минусы remote work. И если по началу большинству людей нравилась работать дома,  то со временем они начали уставать от однообразия и монотонности. 
Неплохим решением для многих стали коворкинги – центры, в которых арендовать рабочее место может любой желающий.
Бизнесмены, стартаперы, фрилансеры и просто творческие люди поначалу оценили все плюсы работы в таком месте, но в какой-то момент резиденты подобных заведений понимают, что помещения перестают быть друзьями для их бизнеса. И вот почему:
Трудности при проведении встреч
Open-space не самое подходящее место для встречи с партнерами и клиентами. Согласитесь, не очень хочется, чтобы вокруг тебя находились “лишние уши”. Вашему приглашенному может быть неловко, к тому же, большинство считает такой формат встреч непрестижным.
Резиденты коворкинга Qubity Space могут бесплатно воспользоваться оборудованной переговорной с шумоизоляцией, где точно никто не подслушает и не будет мешать. Если у вас несколько встреч подряд и на предыдущей вы задержались или клиент приехал раньше, то наши приветливые администраторы встретят вашего гостя, проводят его в комнату отдыха, где он сможет комфортно подождать.
Шумный open-space
Посетители большинства коворкингов страдают от шума и невозможности сосредоточиться, когда вокруг много людей. 
В нашем пространстве действует система штрафов - если резидент ведет себя шумно и мешает остальным, администратор сделает ему замечание. За 3 замечания резидент попадает в черный список и не имеет права посещать коворкинг 1 месяц.
Нет гарантии безопасности
Посетить коворкинг может любой человек, который заплатил за аренду места.  Но поскольку на этих площадях часто обитают люди с улицы, степень безопасности личных вещей и идей сокращается. 
В Qubity Space каждый резидент имеет собственный локер, может зайти только по карте-ключу и Face ID, все пространство оборудовано камерами, а за порядком следят администраторы.
Несовпадение графиков
Многие коворкинги уже перешли на круглосуточный режим работы, но еще не везде вы можете поработать в любые часы, и приходится подстраиваться.
Если вы арендуете закрепленное место у нас, то вы можете прийти поработать в любое время суток, даже ночью.
Платная техника, кофе, снеки
Коворкинг - место для работы, отдохнуть и поесть можно дома, или, на крайний случай, в ближайшем кафе.
Мы там не считаем - резиденты Qubity Space вместе с удобным рабочим местом получают еще и неограниченный кофе, фрукты и снеки, бесплатно могут пользоваться любой офисной техникой.

В Qubity Space мы пострались развеять все мифы о работе в коворкингах и сделать пространство максимально комфортным для вашей продуктивности. Будем рады видеть вас в числе наших резидентов!''')
                await asyncio.sleep(86400)
                await message.answer('''Дизайнерский ремонт в современном стиле, панорамные окна, собственный спортзал и кухня - видеообзор пространства Qubity Space

Неважно, успели вы посетить наш коворкинг или еще нет, вы можете посмотреть, как выглядит наше пространство внутри в небольшом видео.
Будучи резидентом, вы сможете посещать все эти зоны и использовать все преимущества коворкинга.
Приятного просмотра!''')
                await asyncio.sleep(86400)
                await message.answer('''Почему работая в коворкинге ты намного быстрее станешь лучше как специалист и начнешь больше зарабатывать? - отзыв от резидента Qubity Space

Меня зовут Дмитрий, я занимаюсь созданием сайтов уже более 8 лет, 5 лет из которых я работаю на фрилансе. Изначально, когда ушел из офиса, работал дома или в кофейне неподалеку. Понял, что работа из дома дается мне нелегко - не могу сосредоточиться, а в кофейне шумно и не всегда есть место, где можно сесть.
Поэтому стал искать коворкинг в Москве, чтобы было удобно и недалеко от меня.
За пару лет поменял несколько мест, где-то нравилось больше, где-то меньше, но везде были свои недостатки. Для работы мне важна тишина, удобное рабочее место и круглосуточный доступ, т.к. иногда люблю зависнуть над проектом до 12 ночи. В большинстве коворкингов этого не хватало.
Пару месяцев назад друг посоветовал посетить коворкинг Qubity Space. Подкупило, что он находится недалеко от моего дома (15 минут пешком). Пришел на тестовый день и уже работаю там с июня. Это потрясающее место. Если судить по внешним факторам — это пожалуй лучшее место, что я встречал. Сразу как попадаешь сюда, интерьер очень подкупает. Внутри все очень красиво и аккуратно. Отличные удобные офисные кресла и столы. Еще мне особенно нравится то, что коворкинг расположен в бизнес-центре в окружении разных заведений и с развитой инфраструктурой. Есть большой выбор, куда сходить на обед. К тому же можно перекусить прямо в самом коворкинге - тут есть большая просторная кухня с бесплатным кофе. 
Что еще поразило - это абсолютная тишина, почти как в библиотеке. Штрафы за шум, конечно, жестко, зато дисциплина отличная. 
Здесь есть удобная выделенная переговорная с проектором, чего я не встречал в остальных коворкингах.
Еще огромный плюс в пользу Qubity Space - можно работать круглосуточно, если арендовать закрепленное место или офис. Никто в 20:00 не выгоняет, как было на моем предыдущем опыте.
Еще один момент, нельзя снимать коворкинг посуточно или на неделю. Только на месяц, по словам администраторов, этим ограничением они хотят избежать текучки людей и создать дружественную среду, где люди между собой знакомы. Что ж, цель хорошая.

В общем, это отличное место для работы, особенно если вы устали от “домашнего офиса”. Обстановка настраивает на рабочий лад.''')
                await asyncio.sleep(86400*3)
                media = types.MediaGroup()
                media.attach_photo("https://i.imgur.com/d2JHzX7.jpg")
                media.attach_photo("https://i.imgur.com/C1Nue4Q.jpg")
                media.attach_photo("https://i.imgur.com/9Zkuyo5.jpg", '''От чего зависит успех деловой встречи?Конечно же от обстановки!

Естественно важны и другие факторы, например, ваша подготовка, внешний вид, умение презентовать и договариваться. Но даже это все не поможет, если проводить переговоры в неподходящем месте.
Это мы учли в наших переговорных комнатах, ведь именно по обстановке зачастую партнеры или гости судят о солидности мероприятия в целом.

В комнате для переговоров имеется:
проектор
флип-чарт
стабильный быстрый Wi-Fi

🚪Арендуемая площадь - 18 кв.м.

🎎Зал вмещает до 10 человек, мебель стоит по принципу «Круглый стол», также по запросу возможна «театральная» расстановка кресел.

☕️Для комфортного проведения деловых мероприятий у вас будет неограниченный доступ к напиткам, фруктам и снекам. Также в перерыве вы можете разместиться в удобной конмнате отдыха и передохнуть.

Каждый резидент с закрепленным рабочим местом получает доступ к переговорной совершенно бесплатно и может забранировать ее от 1 ч в день.''')
                await message.bot.send_media_group(message.chat.id, media=media)
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Какое время работы локаций и есть ли парковка - ответили на самые популярные вопросы о коворкинге Qubity Space 

Можно ли приводить гостей, если у меня самого тестовый день? А прийти на него второй раз в другую локацию?
Пробный день в коворкинге создан для того, чтобы вы могли прочувствовать атмосферу работы в Qubity Space. Если вы уже побывали в одной из локаций и хотите поработать в течение дня в другой, обратите внимание на тариф “Гость”. Если вам необходимо провести встречу, рекомендуем рассмотреть возможность аренды переговорных комнат или также воспользоваться тарифом “Гость”, включающим посещение 1 гостя.
Где можно припарковаться? 
В Qubity Space обратите внимание на подземную парковку или наземную парковку БЦ “Нео Гео”. Позвоните администратору коворкинга заранее, чтобы узнать, доступно ли парковочное место в запланированное вами время посещения коворкинга. Также на срок от 1 месяца возможно арендовать парковочное место в БЦ.
У вас в офисах есть мебель? Можно ли привезти свою? 
Каждый офис Qubity Space оборудован столами и креслами в соответствии с количеством рабочих мест в нем. Обустроить кабинет вы можете на своё усмотрение (только не забудьте предварительно оповестить администратора, если вы собираетесь вносить в коворкинг что-то крупногабаритное). Если мы получаем от резидентов большое количество запросов на какой-то определённый тип мебели (например, тумбы), рассматриваем возможность дополнить обустройство рабочих мест. Также мы предоставляем в аренду персональные локеры.
Время работы локаций? 
Для резидентов, выбравших тариф "Резидент" или Smart-офис коворкинг открыт круглосуточно. Для резидентов коворкинга, выбравших тариф “Гость”, – с 8:00 до 20:00, в рабочее время команды локации.
Как осуществляется охрана коворкинга? 
Вход в коворкинг осуществляется строго по пропускам резидентов и Face-ID. Также в офисных пространствах установлены камеры видеонаблюдения, к записям с которых в случае необходимости мы можем обратиться. Каждый резидент получает собственный локер для хранения личных вещей, а за порядком следят администраторы.
Вы предоставляете юридический адрес?
Юридический адрес является дополнительной услугой и предоставляется только арендаторам кабинетов, выбравшим срок аренды от 11 месяцев, а также арендой от 25 мест. Вначале мы заключаем с вами договор субаренды, затем вы оплачиваете услугу, и мы готовим подтверждающие вашу работу в офисном пространстве документы для налоговой.
Как организовать мероприятие на вашей площадке? 
Если вы уже определились с датой, ознакомьтесь со свободными временными окнами у администраторов пространства. Если дата свободна, можно приступать к обсуждению деталей события: какое техническое оснащение для него потребуются, какой формат рассадки предполагается, какое количество гостей вы ожидаете увидеть. Во всех наших локациях действует пропускная система, поэтому не забудьте при регистрации запросить у гостей их полные ФИО.

Если у вас остались вопросы, то вы можете задать их администраторам коворкинга Qubity, написав боту в ответ на это сообщение или по телефону: +7 (926) 911-13-96.''')
                q = await User.question.set()
                await asyncio.sleep(86400*3)
                if not q:
                    await message.answer('''Что можно купить за 450 Р? 2 чашки кофе или 1 день в современном коворкинге Qubity Space и пить кофе в неограниченном количестве

Стоимость размещения в коворкинге зависит от того, арендуете вы незакрепленное место в open space или закрепленное в офисе, а также от времени доступа в коворкинг. 

Наши тарифы:

Гость - 1000 Р/день
Незакрепленное место в openspace
Доступ 1 день (8:00-20:00)
Кофе-брейки
Лаундж-зона (30 мин.)
Skype-room (30 мин.)
Все общие зоны

Резидент Light - 14.500 Р/месяц
Незакрепленное место в openspace
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Резидент Platinum - 18.500 Р/месяц
Закрепленное место в Smart-офисе
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Smart-офис - от 16.000 Р/чел
Индивидуальный Smart-офис
Доступ 24/7
Кофе-брейки
Лаундж-зона (от 1 ч./день)
Skype-room (от 1 ч./день)
Все общие зоны

Приходите на бесплатный день в коворкинге Qubity Space, чтобы подобрать тариф для себя
Переходите по ссылке на наш сайт, чтобы забронировать бесплатное место в коворкинге: http://qubity.space/''')
                    await state.finish()
                    
            elif beh[6] == "Мероприятия/переговорки":
                await message.answer('''Спасибо, мы приняли Ваши контактные данные и забронировали 1 бесплатный день за Вашим номером телефона. 

Что Вас ждет на тестовом дне в коворкинге Qubity Space:
 - 612 м2 пространства для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении
 - удобное рабочее место в тихом open-space для максимально комфортной работы
 - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1 ч)
 - пользование Skype-кабиной для созвонов с шумопоглощением (до 1 ч)
 - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном
 - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой
А еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный Wi-fi

Совсем скоро с вами свяжется Ваш менеджер, уточнит детали вашего визита и ответит на ваши вопросы.

В следующем сообщении Вы получите обещанный бонус: чек-лист для повышения продуктивности работы в офисе''')
                await asyncio.sleep(28800)
                await message.answer('''Как выбрать помещение, чтобы повысить эффективность тренингов и переговоров?

Конечно, у плохого танцора, помехи никак не связаны с профессионализмом. Тренинг можно провести в любых условиях:
 - и в подвальном банкетном зале,
 - и в зале ресторана,
 - и параллельно обслуживая клиентов…
Любой раздражающий фактор можно минимизировать, но нужна ли эта борьба на ровном месте?

Вот несколько моментов, на которые стоит обратить внимание, выбирая, где провести тренинг:

Изолированное. Посетители и звонки должны остаться за дверью.
Тихое. Стройка за окном, шум оборудования, музыка за стенкой, работающая пожарная сигнализация – не лучший аккомпанемент. Акустику тоже лучше проверить заранее.
Комфортное. 20 градусов чистого воздуха – то, что надо. Тепло зимой, прохладно летом. Работающая вентиляция или возможность открыть окно. Кондиционер и жалюзи летом.
Светлое. Света должно быть достаточно, чтобы читать, меньшая освещённость загоняет в спячку. Отсутствие окон – сильный недостаток, люди быстрее устают.
Просторное. Нужно без помех посадить всех участников полукругом, чтобы с любого места было нормально видно доску, экран. Никаких школьных парт.
Оборудованное всем необходимым. Чаще всего может понадобиться флипчарт, проектор, маркеры. Это можно принести и самому, но будет лучше, если вам не придется переживать, что вы что-то забыли.

Хороший ланч вряд ли вытянет провальный тренинг, зато его отсутствие — испортит даже самую прекрасную программу. Учесть стоит всё:
Организация обедов.
Если имеем дело с доставкой, важно, чтобы привезли вовремя, иначе ломается весь график.
Кофе-брейки.
Идеальное место для кофе-брейка – соседняя комната, а вот кулер или запас бутылок с водой должны быть непосредственно в зале. Необходимость перейти на другой этаж, чтобы попить кофе, сразу превращает 15-минутный перерыв в получасовой. 
Указатели, если не все участники знают дорогу.

В нашем коворкинге есть большая переговорная комната на 30 человек. Она оборудована всем необходимым для комфортного проведения тренингов и переговоров: здесь есть проектор, флипчарт, удобные столы и стулья, шумоизоляция и большие панорамные окна. Также ввм не придется переживать о бизнес-ланчах и перекусах - в пространстве есть удобная кухня с бесплатным кофе и снеками, а для заказа обеда можно вызвать курьера.

Эти простые советы помогут не только подобрать помещение для тренинга, но и увеличить его эффективность и уменьшить время и средства на подготовку.

Оценить наше помещение для переговоров в Qubity Space вы сможете на бесплатном посещении.

В следующих сообщениях Вы получите больше информации о нашем коворинге.''')
                await asyncio.sleep(86400)
                await message.answer('''Ошибки коворкингов, которые учтены в Qubity Space

Удаленная работа из дома. В 2020 году все люди принудительно узнали, что это такое и ощутили на себе все плюсы и минусы remote work. И если по началу большинству людей нравилась работать дома,  то со временем они начали уставать от однообразия и монотонности. 
Неплохим решением для многих стали коворкинги – центры, в которых арендовать рабочее место может любой желающий.
Бизнесмены, стартаперы, фрилансеры и просто творческие люди поначалу оценили все плюсы работы в таком месте, но в какой-то момент резиденты подобных заведений понимают, что помещения перестают быть друзьями для их бизнеса. И вот почему:
Трудности при проведении встреч
Open-space не самое подходящее место для встречи с партнерами и клиентами. Согласитесь, не очень хочется, чтобы вокруг тебя находились “лишние уши”. Вашему приглашенному может быть неловко, к тому же, большинство считает такой формат встреч непрестижным.
Резиденты коворкинга Qubity Space могут бесплатно воспользоваться оборудованной переговорной с шумоизоляцией, где точно никто не подслушает и не будет мешать. Если у вас несколько встреч подряд и на предыдущей вы задержались или клиент приехал раньше, то наши приветливые администраторы встретят вашего гостя, проводят его в комнату отдыха, где он сможет комфортно подождать.
Шумный open-space
Посетители большинства коворкингов страдают от шума и невозможности сосредоточиться, когда вокруг много людей. 
В нашем пространстве действует система штрафов - если резидент ведет себя шумно и мешает остальным, администратор сделает ему замечание. За 3 замечания резидент попадает в черный список и не имеет права посещать коворкинг 1 месяц.
Нет гарантии безопасности
Посетить коворкинг может любой человек, который заплатил за аренду места.  Но поскольку на этих площадях часто обитают люди с улицы, степень безопасности личных вещей и идей сокращается. 
В Qubity Space каждый резидент имеет собственный локер, может зайти только по карте-ключу и Face ID, все пространство оборудовано камерами, а за порядком следят администраторы.
Несовпадение графиков
Многие коворкинги уже перешли на круглосуточный режим работы, но еще не везде вы можете поработать в любые часы, и приходится подстраиваться.
Если вы арендуете закрепленное место у нас, то вы можете прийти поработать в любое время суток, даже ночью.
Платная техника, кофе, снеки
Коворкинг - место для работы, отдохнуть и поесть можно дома, или, на крайний случай, в ближайшем кафе.
Мы там не считаем - резиденты Qubity Space вместе с удобным рабочим местом получают еще и неограниченный кофе, фрукты и снеки, бесплатно могут пользоваться любой офисной техникой.

В Qubity Space мы пострались развеять все мифы о работе в коворкингах и сделать пространство максимально комфортным для вашей продуктивности. Будем рады видеть вас в числе наших резидентов!''')
                await asyncio.sleep(86400)
                await message.answer('''Дизайнерский ремонт в современном стиле, панорамные окна, собственный спортзал и кухня - видеообзор пространства Qubity Space

Неважно, успели вы посетить наш коворкинг или еще нет, вы можете посмотреть, как выглядит наше пространство внутри в небольшом видео.
Будучи резидентом, вы сможете посещать все эти зоны и использовать все преимущества коворкинга.
Приятного просмотра!''')
                await asyncio.sleep(86400)
                await message.answer('''Почему работая в коворкинге ты намного быстрее станешь лучше как специалист и начнешь больше зарабатывать? - отзыв от резидента Qubity Space

Меня зовут Дмитрий, я занимаюсь созданием сайтов уже более 8 лет, 5 лет из которых я работаю на фрилансе. Изначально, когда ушел из офиса, работал дома или в кофейне неподалеку. Понял, что работа из дома дается мне нелегко - не могу сосредоточиться, а в кофейне шумно и не всегда есть место, где можно сесть.
Поэтому стал искать коворкинг в Москве, чтобы было удобно и недалеко от меня.
За пару лет поменял несколько мест, где-то нравилось больше, где-то меньше, но везде были свои недостатки. Для работы мне важна тишина, удобное рабочее место и круглосуточный доступ, т.к. иногда люблю зависнуть над проектом до 12 ночи. В большинстве коворкингов этого не хватало.
Пару месяцев назад друг посоветовал посетить коворкинг Qubity Space. Подкупило, что он находится недалеко от моего дома (15 минут пешком). Пришел на тестовый день и уже работаю там с июня. Это потрясающее место. Если судить по внешним факторам — это пожалуй лучшее место, что я встречал. Сразу как попадаешь сюда, интерьер очень подкупает. Внутри все очень красиво и аккуратно. Отличные удобные офисные кресла и столы. Еще мне особенно нравится то, что коворкинг расположен в бизнес-центре в окружении разных заведений и с развитой инфраструктурой. Есть большой выбор, куда сходить на обед. К тому же можно перекусить прямо в самом коворкинге - тут есть большая просторная кухня с бесплатным кофе. 
Что еще поразило - это абсолютная тишина, почти как в библиотеке. Штрафы за шум, конечно, жестко, зато дисциплина отличная. 
Здесь есть удобная выделенная переговорная с проектором, чего я не встречал в остальных коворкингах.
Еще огромный плюс в пользу Qubity Space - можно работать круглосуточно, если арендовать закрепленное место или офис. Никто в 20:00 не выгоняет, как было на моем предыдущем опыте.
Еще один момент, нельзя снимать коворкинг посуточно или на неделю. Только на месяц, по словам администраторов, этим ограничением они хотят избежать текучки людей и создать дружественную среду, где люди между собой знакомы. Что ж, цель хорошая.

В общем, это отличное место для работы, особенно если вы устали от “домашнего офиса”. Обстановка настраивает на рабочий лад.''')
                await asyncio.sleep(86400*3)
                media = types.MediaGroup()
                media.attach_photo("https://i.imgur.com/d2JHzX7.jpg")
                media.attach_photo("https://i.imgur.com/C1Nue4Q.jpg")
                media.attach_photo("https://i.imgur.com/9Zkuyo5.jpg", '''От чего зависит успех деловой встречи?Конечно же от обстановки!

Естественно важны и другие факторы, например, ваша подготовка, внешний вид, умение презентовать и договариваться. Но даже это все не поможет, если проводить переговоры в неподходящем месте.
Это мы учли в наших переговорных комнатах, ведь именно по обстановке зачастую партнеры или гости судят о солидности мероприятия в целом.

В комнате для переговоров имеется:
проектор
флип-чарт
стабильный быстрый Wi-Fi

🚪Арендуемая площадь - 18 кв.м.

🎎Зал вмещает до 10 человек, мебель стоит по принципу «Круглый стол», также по запросу возможна «театральная» расстановка кресел.

☕️Для комфортного проведения деловых мероприятий у вас будет неограниченный доступ к напиткам, фруктам и снекам. Также в перерыве вы можете разместиться в удобной конмнате отдыха и передохнуть.

Каждый резидент с закрепленным рабочим местом получает доступ к переговорной совершенно бесплатно и может забранировать ее от 1 ч в день.''')
                await message.bot.send_media_group(message.chat.id, media=media)
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Какое время работы локаций и есть ли парковка - ответили на самые популярные вопросы о коворкинге Qubity Space 

Можно ли приводить гостей, если у меня самого тестовый день? А прийти на него второй раз в другую локацию?
Пробный день в коворкинге создан для того, чтобы вы могли прочувствовать атмосферу работы в Qubity Space. Если вы уже побывали в одной из локаций и хотите поработать в течение дня в другой, обратите внимание на тариф “Гость”. Если вам необходимо провести встречу, рекомендуем рассмотреть возможность аренды переговорных комнат или также воспользоваться тарифом “Гость”, включающим посещение 1 гостя.
Где можно припарковаться? 
В Qubity Space обратите внимание на подземную парковку или наземную парковку БЦ “Нео Гео”. Позвоните администратору коворкинга заранее, чтобы узнать, доступно ли парковочное место в запланированное вами время посещения коворкинга. Также на срок от 1 месяца возможно арендовать парковочное место в БЦ.
У вас в офисах есть мебель? Можно ли привезти свою? 
Каждый офис Qubity Space оборудован столами и креслами в соответствии с количеством рабочих мест в нем. Обустроить кабинет вы можете на своё усмотрение (только не забудьте предварительно оповестить администратора, если вы собираетесь вносить в коворкинг что-то крупногабаритное). Если мы получаем от резидентов большое количество запросов на какой-то определённый тип мебели (например, тумбы), рассматриваем возможность дополнить обустройство рабочих мест. Также мы предоставляем в аренду персональные локеры.
Время работы локаций? 
Для резидентов, выбравших тариф "Резидент" или Smart-офис коворкинг открыт круглосуточно. Для резидентов коворкинга, выбравших тариф “Гость”, – с 8:00 до 20:00, в рабочее время команды локации.
Как осуществляется охрана коворкинга? 
Вход в коворкинг осуществляется строго по пропускам резидентов и Face-ID. Также в офисных пространствах установлены камеры видеонаблюдения, к записям с которых в случае необходимости мы можем обратиться. Каждый резидент получает собственный локер для хранения личных вещей, а за порядком следят администраторы.
Вы предоставляете юридический адрес?
Юридический адрес является дополнительной услугой и предоставляется только арендаторам кабинетов, выбравшим срок аренды от 11 месяцев, а также арендой от 25 мест. Вначале мы заключаем с вами договор субаренды, затем вы оплачиваете услугу, и мы готовим подтверждающие вашу работу в офисном пространстве документы для налоговой.
Как организовать мероприятие на вашей площадке? 
Если вы уже определились с датой, ознакомьтесь со свободными временными окнами у администраторов пространства. Если дата свободна, можно приступать к обсуждению деталей события: какое техническое оснащение для него потребуются, какой формат рассадки предполагается, какое количество гостей вы ожидаете увидеть. Во всех наших локациях действует пропускная система, поэтому не забудьте при регистрации запросить у гостей их полные ФИО.

Если у вас остались вопросы, то вы можете задать их администраторам коворкинга Qubity, написав боту в ответ на это сообщение или по телефону: +7 (926) 911-13-96.''')
                q = await User.question.set()
                await asyncio.sleep(86400*3)
                if not q:
                    await message.answer('''Что можно купить за 450 Р? 2 чашки кофе или 1 день в современном коворкинге Qubity Space и пить кофе в неограниченном количестве

Стоимость размещения в коворкинге зависит от того, арендуете вы незакрепленное место в open space или закрепленное в офисе, а также от времени доступа в коворкинг. 

Наши тарифы:

Гость - 1000 Р/день
Незакрепленное место в openspace
Доступ 1 день (8:00-20:00)
Кофе-брейки
Лаундж-зона (30 мин.)
Skype-room (30 мин.)
Все общие зоны

Резидент Light - 14.500 Р/месяц
Незакрепленное место в openspace
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Резидент Platinum - 18.500 Р/месяц
Закрепленное место в Smart-офисе
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Smart-офис - от 16.000 Р/чел
Индивидуальный Smart-офис
Доступ 24/7
Кофе-брейки
Лаундж-зона (от 1 ч./день)
Skype-room (от 1 ч./день)
Все общие зоны

Приходите на бесплатный день в коворкинге Qubity Space, чтобы подобрать тариф для себя
Переходите по ссылке на наш сайт, чтобы забронировать бесплатное место в коворкинге: http://qubity.space/''')
                    await state.finish()
                
            elif beh[6] == "Рабочее место с форматом все включено":
                await message.answer('''Спасибо, мы приняли Ваши контактные данные и забронировали 1 бесплатный день за Вашим номером телефона. 

Что Вас ждет на тестовом дне в коворкинге Qubity Space:
 - 612 м2 пространства для сильного бизнес-сообщества предпринимателей и специалистов в вашем распоряжении
 - удобное рабочее место в тихом open-space для максимально комфортной работы
 - доступ в оборудованную переговорную комнату и конференц-зал на 15 человек (до 1 ч)
 - пользование Skype-кабиной для созвонов с шумопоглощением (до 1 ч)
 - отдых в приватной лаундж-зоне с мягкими креслами и панорамным окном
 - посещение work out и игровой зоны с турником, брусьями, гантелями и скакалкой
А еще неограниченный кофе, фрукты, снеки, офисная техника и скоростной стабильный Wi-fi

Совсем скоро с вами свяжется Ваш менеджер, уточнит детали вашего визита и ответит на ваши вопросы.

В следующем сообщении Вы получите обещанный бонус: чек-лист для повышения продуктивности работы в офисе''')
                await asyncio.sleep(28800)
                await message.answer('''Как рабочая обстановка помогает бороться с эмоциональным выгоранием и увеличивает продуктивность

Последние тенденции общества направлены на поддержание не только физического, но и ментального здоровья. Так как работа занимает большую часть нашей повседневной жизни, специалисты все чаще жалуются на стресс, хроническую усталость и раздражительность. Психологи называют такое состояние эмоциональным выгоранием. Исследование сервисов HeadHunter и “Доктор рядом” за 2020 год показало, что половина из 2,5 тысяч опрошенных работников испытывают тревогу, чуть меньше опрошенных (48%) из-за переутомления стали эмоционально бесчувственными, работают на автомате и ощущают опустошение при выполнении задач. 45% респондентов испытывают личностное отчуждение по отношению к коллегам.
Если вы тоже замечаете за собой такое состояние или его зачатки, то вот Х советов, которые помогут вам справиться с выгоранием и увеличить продуктивность без смены работы и психотерапевта:
Заботьтесь о своем здоровье. 
Сбалансированно питайтесь, наладьте режим сна, занимайтесь спортом, гуляйте на свежем воздухе и полноценно отдыхайте в выходные.
Научитесь отключаться от работы
Многим людям с “синдромом менеджера” сложно найти время на отдых и отвлечься от работы. Но это необходимо, чтобы восстановиться и не растерять мотивацию. Например, в нашем коворкинге Qubity Space есть комната для отдыха с удобными креслами и игровая зона с турником, брусьями, гантелями и скакалкой. Здесь вы не только сделаете перерыв, но и сможете подтянуть свою физическую форму.
Следите за уровнем стресса
Даже если вам кажется, что стресс - неотъемлимая часть вашей жизни и от него нельзя избавиться, то вы ошибаетесь. Значительно уменьшить его влияние помогут рефлексия, медитация, дыхательные практики, а также смена обстановки. 
Поговорите с тем, кому вы доверяете
Это может быть друг, партнер, родители, коллега. Общение с приятными людьми помогает нам расслабиться, поделиться своими чувствами и эмоциями. В нашем коворкинге вы можете работать вместе с коллегами, а также найти новые знакомства среди сильных специалистов в вашей сфере, которые в будущем могут стать вашими друзьями или партнерами.
Сохраняйте свои личные границы
Если игнорировать собственные эмоции и позволять их постоянно нарушать, то рано или поздно вы сталкнетесь с симптомами выгорания. Чтобы такого не произошло, научитесь говорить нет, сократите контакты с неприятными людьми, уберите все раздражители, особенно на работе. Выбирая для работы офис в коворкинге Qubity Space, вы будете находиться в изолированном пространстве, где вас не будут отвлекать и тревожить, чтобы вы могли сосредоточиться на своих задачах без чужого вмешательства.
Планируйте отдых
Очень сложно расслабиться, когда 24/7 думаете о работе. Поэтому важно выделять в своём расписании перерывы на отдых. Например, в нашем пространстве есть оборудованная кухня с кофемашиной, куда вы можете отойти, чтобы сделать вкусный кофе и перекусить фруктами и полезными снеками и еще быстрее восстановить силы. 
Обустройте рабочее место. 
Для продуктивной работы (и здоровой спины) нужен удобный стол и стул, достаточно света и свежего воздуха. В наших офисах настроена система вентиляции, большие окна и много света, чтобы вы могли чувствовать себя хорошо ментально и физически.

Эти простые советы помогут  не только справиться с симптомами эмоцианального выгорания, но и приобрести полезные привычки для вашей повседневной жизни.

Ощутимо повысить продуктивность за 1 день вы сможете на бесплатном посещении нашего коворкинга Qubity Space.

В следующих сообщениях Вы получите больше информации о нашем коворинге.''')
                await asyncio.sleep(86400)
                await message.answer('''Ошибки коворкингов, которые учтены в Qubity Space

Удаленная работа из дома. В 2020 году все люди принудительно узнали, что это такое и ощутили на себе все плюсы и минусы remote work. И если по началу большинству людей нравилась работать дома,  то со временем они начали уставать от однообразия и монотонности. 
Неплохим решением для многих стали коворкинги – центры, в которых арендовать рабочее место может любой желающий.
Бизнесмены, стартаперы, фрилансеры и просто творческие люди поначалу оценили все плюсы работы в таком месте, но в какой-то момент резиденты подобных заведений понимают, что помещения перестают быть друзьями для их бизнеса. И вот почему:
Трудности при проведении встреч
Open-space не самое подходящее место для встречи с партнерами и клиентами. Согласитесь, не очень хочется, чтобы вокруг тебя находились “лишние уши”. Вашему приглашенному может быть неловко, к тому же, большинство считает такой формат встреч непрестижным.
Резиденты коворкинга Qubity Space могут бесплатно воспользоваться оборудованной переговорной с шумоизоляцией, где точно никто не подслушает и не будет мешать. Если у вас несколько встреч подряд и на предыдущей вы задержались или клиент приехал раньше, то наши приветливые администраторы встретят вашего гостя, проводят его в комнату отдыха, где он сможет комфортно подождать.
Шумный open-space
Посетители большинства коворкингов страдают от шума и невозможности сосредоточиться, когда вокруг много людей. 
В нашем пространстве действует система штрафов - если резидент ведет себя шумно и мешает остальным, администратор сделает ему замечание. За 3 замечания резидент попадает в черный список и не имеет права посещать коворкинг 1 месяц.
Нет гарантии безопасности
Посетить коворкинг может любой человек, который заплатил за аренду места.  Но поскольку на этих площадях часто обитают люди с улицы, степень безопасности личных вещей и идей сокращается. 
В Qubity Space каждый резидент имеет собственный локер, может зайти только по карте-ключу и Face ID, все пространство оборудовано камерами, а за порядком следят администраторы.
Несовпадение графиков
Многие коворкинги уже перешли на круглосуточный режим работы, но еще не везде вы можете поработать в любые часы, и приходится подстраиваться.
Если вы арендуете закрепленное место у нас, то вы можете прийти поработать в любое время суток, даже ночью.
Платная техника, кофе, снеки
Коворкинг - место для работы, отдохнуть и поесть можно дома, или, на крайний случай, в ближайшем кафе.
Мы там не считаем - резиденты Qubity Space вместе с удобным рабочим местом получают еще и неограниченный кофе, фрукты и снеки, бесплатно могут пользоваться любой офисной техникой.

В Qubity Space мы пострались развеять все мифы о работе в коворкингах и сделать пространство максимально комфортным для вашей продуктивности. Будем рады видеть вас в числе наших резидентов!''')
                await asyncio.sleep(86400)
                await message.answer('''Дизайнерский ремонт в современном стиле, панорамные окна, собственный спортзал и кухня - видеообзор пространства Qubity Space

Неважно, успели вы посетить наш коворкинг или еще нет, вы можете посмотреть, как выглядит наше пространство внутри в небольшом видео.
Будучи резидентом, вы сможете посещать все эти зоны и использовать все преимущества коворкинга.
Приятного просмотра!''')
                await asyncio.sleep(86400)
                await message.answer('''Почему работая в коворкинге ты намного быстрее станешь лучше как специалист и начнешь больше зарабатывать? - отзыв от резидента Qubity Space

Меня зовут Дмитрий, я занимаюсь созданием сайтов уже более 8 лет, 5 лет из которых я работаю на фрилансе. Изначально, когда ушел из офиса, работал дома или в кофейне неподалеку. Понял, что работа из дома дается мне нелегко - не могу сосредоточиться, а в кофейне шумно и не всегда есть место, где можно сесть.
Поэтому стал искать коворкинг в Москве, чтобы было удобно и недалеко от меня.
За пару лет поменял несколько мест, где-то нравилось больше, где-то меньше, но везде были свои недостатки. Для работы мне важна тишина, удобное рабочее место и круглосуточный доступ, т.к. иногда люблю зависнуть над проектом до 12 ночи. В большинстве коворкингов этого не хватало.
Пару месяцев назад друг посоветовал посетить коворкинг Qubity Space. Подкупило, что он находится недалеко от моего дома (15 минут пешком). Пришел на тестовый день и уже работаю там с июня. Это потрясающее место. Если судить по внешним факторам — это пожалуй лучшее место, что я встречал. Сразу как попадаешь сюда, интерьер очень подкупает. Внутри все очень красиво и аккуратно. Отличные удобные офисные кресла и столы. Еще мне особенно нравится то, что коворкинг расположен в бизнес-центре в окружении разных заведений и с развитой инфраструктурой. Есть большой выбор, куда сходить на обед. К тому же можно перекусить прямо в самом коворкинге - тут есть большая просторная кухня с бесплатным кофе. 
Что еще поразило - это абсолютная тишина, почти как в библиотеке. Штрафы за шум, конечно, жестко, зато дисциплина отличная. 
Здесь есть удобная выделенная переговорная с проектором, чего я не встречал в остальных коворкингах.
Еще огромный плюс в пользу Qubity Space - можно работать круглосуточно, если арендовать закрепленное место или офис. Никто в 20:00 не выгоняет, как было на моем предыдущем опыте.
Еще один момент, нельзя снимать коворкинг посуточно или на неделю. Только на месяц, по словам администраторов, этим ограничением они хотят избежать текучки людей и создать дружественную среду, где люди между собой знакомы. Что ж, цель хорошая.

В общем, это отличное место для работы, особенно если вы устали от “домашнего офиса”. Обстановка настраивает на рабочий лад.''')
                await asyncio.sleep(86400*3)
                media = types.MediaGroup()
                media.attach_photo("https://i.imgur.com/d2JHzX7.jpg")
                media.attach_photo("https://i.imgur.com/C1Nue4Q.jpg")
                media.attach_photo("https://i.imgur.com/9Zkuyo5.jpg", '''От чего зависит успех деловой встречи?Конечно же от обстановки!

Естественно важны и другие факторы, например, ваша подготовка, внешний вид, умение презентовать и договариваться. Но даже это все не поможет, если проводить переговоры в неподходящем месте.
Это мы учли в наших переговорных комнатах, ведь именно по обстановке зачастую партнеры или гости судят о солидности мероприятия в целом.

В комнате для переговоров имеется:
проектор
флип-чарт
стабильный быстрый Wi-Fi

🚪Арендуемая площадь - 18 кв.м.

🎎Зал вмещает до 10 человек, мебель стоит по принципу «Круглый стол», также по запросу возможна «театральная» расстановка кресел.

☕️Для комфортного проведения деловых мероприятий у вас будет неограниченный доступ к напиткам, фруктам и снекам. Также в перерыве вы можете разместиться в удобной конмнате отдыха и передохнуть.

Каждый резидент с закрепленным рабочим местом получает доступ к переговорной совершенно бесплатно и может забранировать ее от 1 ч в день.''')
                await message.bot.send_media_group(message.chat.id, media=media)
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
                await asyncio.sleep(86400*3)
                await message.answer('''Какое время работы локаций и есть ли парковка - ответили на самые популярные вопросы о коворкинге Qubity Space 

Можно ли приводить гостей, если у меня самого тестовый день? А прийти на него второй раз в другую локацию?
Пробный день в коворкинге создан для того, чтобы вы могли прочувствовать атмосферу работы в Qubity Space. Если вы уже побывали в одной из локаций и хотите поработать в течение дня в другой, обратите внимание на тариф “Гость”. Если вам необходимо провести встречу, рекомендуем рассмотреть возможность аренды переговорных комнат или также воспользоваться тарифом “Гость”, включающим посещение 1 гостя.
Где можно припарковаться? 
В Qubity Space обратите внимание на подземную парковку или наземную парковку БЦ “Нео Гео”. Позвоните администратору коворкинга заранее, чтобы узнать, доступно ли парковочное место в запланированное вами время посещения коворкинга. Также на срок от 1 месяца возможно арендовать парковочное место в БЦ.
У вас в офисах есть мебель? Можно ли привезти свою? 
Каждый офис Qubity Space оборудован столами и креслами в соответствии с количеством рабочих мест в нем. Обустроить кабинет вы можете на своё усмотрение (только не забудьте предварительно оповестить администратора, если вы собираетесь вносить в коворкинг что-то крупногабаритное). Если мы получаем от резидентов большое количество запросов на какой-то определённый тип мебели (например, тумбы), рассматриваем возможность дополнить обустройство рабочих мест. Также мы предоставляем в аренду персональные локеры.
Время работы локаций? 
Для резидентов, выбравших тариф "Резидент" или Smart-офис коворкинг открыт круглосуточно. Для резидентов коворкинга, выбравших тариф “Гость”, – с 8:00 до 20:00, в рабочее время команды локации.
Как осуществляется охрана коворкинга? 
Вход в коворкинг осуществляется строго по пропускам резидентов и Face-ID. Также в офисных пространствах установлены камеры видеонаблюдения, к записям с которых в случае необходимости мы можем обратиться. Каждый резидент получает собственный локер для хранения личных вещей, а за порядком следят администраторы.
Вы предоставляете юридический адрес?
Юридический адрес является дополнительной услугой и предоставляется только арендаторам кабинетов, выбравшим срок аренды от 11 месяцев, а также арендой от 25 мест. Вначале мы заключаем с вами договор субаренды, затем вы оплачиваете услугу, и мы готовим подтверждающие вашу работу в офисном пространстве документы для налоговой.
Как организовать мероприятие на вашей площадке? 
Если вы уже определились с датой, ознакомьтесь со свободными временными окнами у администраторов пространства. Если дата свободна, можно приступать к обсуждению деталей события: какое техническое оснащение для него потребуются, какой формат рассадки предполагается, какое количество гостей вы ожидаете увидеть. Во всех наших локациях действует пропускная система, поэтому не забудьте при регистрации запросить у гостей их полные ФИО.

Если у вас остались вопросы, то вы можете задать их администраторам коворкинга Qubity, написав боту в ответ на это сообщение или по телефону: +7 (926) 911-13-96.''')
                q = await User.question.set()
                await asyncio.sleep(86400*3)
                if not q:
                    await message.answer('''Что можно купить за 450 Р? 2 чашки кофе или 1 день в современном коворкинге Qubity Space и пить кофе в неограниченном количестве

Стоимость размещения в коворкинге зависит от того, арендуете вы незакрепленное место в open space или закрепленное в офисе, а также от времени доступа в коворкинг. 

Наши тарифы:

Гость - 1000 Р/день
Незакрепленное место в openspace
Доступ 1 день (8:00-20:00)
Кофе-брейки
Лаундж-зона (30 мин.)
Skype-room (30 мин.)
Все общие зоны

Резидент Light - 14.500 Р/месяц
Незакрепленное место в openspace
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Резидент Platinum - 18.500 Р/месяц
Закрепленное место в Smart-офисе
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Smart-офис - от 16.000 Р/чел
Индивидуальный Smart-офис
Доступ 24/7
Кофе-брейки
Лаундж-зона (от 1 ч./день)
Skype-room (от 1 ч./день)
Все общие зоны

Приходите на бесплатный день в коворкинге Qubity Space, чтобы подобрать тариф для себя
Переходите по ссылке на наш сайт, чтобы забронировать бесплатное место в коворкинге: http://qubity.space/''')
                    await state.finish()
                
            
                
        else:
            await message.reply(f'Номер телефона состоит из 9-12 чисел. \nОтправьте мне свой номер телефона заново: ')
            await User.number.set()   
    else:
        await message.reply(f'Отправьте мне свой номер телефона без плюса(+): ')
        await User.number.set()
        

@dp.message_handler(state="*", commands=['start', "menu"])
async def start_msg(message: types.Message, state: FSMContext):
    args = message.get_args()
    if args == "":
        try:
            async with aiosqlite.connect('dbase.db') as con:
                con.row_factory = lambda cursor, row: row[0]
                conn = await con.cursor()
                await conn.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER UNIQUE, name TEXT, number TEXT, a1 TEXT, a1_dt TEXT, a2 TEXT, a2_dt TEXT, a3 TEXT, a3_dt TEXT)')
                await conn.execute('INSERT INTO users VALUES(?,?,?,?,?,?,?,?,?);', (message.from_user.id, message.from_user.first_name, "Не отправлял номер", "Не ответил", "Нету", "Не ответил", "Нету", "Не ответил", "Нету", ))
                await con.commit()
                check = await conn.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
                check = await check.fetchone()
            if not str(check).isdigit():
                await message.answer(f'<b>Здравствуйте, </b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>.'
                             f'\n\nВас приветствует бот-помощник Qubity Space и я подберу для Вас место для работы вне дома.'
                             f'\nДля этого Вам нужно ответить на 3 вопроса. \nНажмите кнопку <b>"Старт"</b>, чтобы начать', reply_markup=Buttons.beginning())
        except sqlite3.IntegrityError as e:
            await message.reply("Вы уже записывались!")
            
            
    if args == "bonus":
        await message.reply('''Супер! Вы сделали все верно :)

Как и обещали, Ваша статья “15 идей как фрилансеру разнообразить свои рабочие будни, чтобы 24/7 не сидеть дома”

“Что бы мне поделать, только бы не поработать?”
Если работая дома вы не можете сосредоточиться и постоянно откладываете задачи на потом, вот 15 советов, которые помогут вам оставаться продуктивным на фрилансе и не сойти с ума:
Планируйте завтрашний день
Составляйте с вечера список дел на завтра.  Зная свои приоритеты, вы не станете тратить время на ерунду и будете меньше отвлекаться.
Научитесь отключаться от работы
Очень сложно перестать думать о работе, когда дом и офис — одно и то же место. Но это необходимо, чтобы восстановиться и не растерять мотивацию. Например, в нашем коворкинге Qubity Space есть комната для отдыха с удобными креслами и игровая зона с турником, брусьями, гантелями и скакалкой. Здесь вы не только сделаете перерыв, но и сможете подтянуть свою физическую форму.
Работайте в определённой одежде
Да, это работает! Многие психологи считают, что как и атмосфера вокруг, одежда может создавать ощущение того, что вы на работе. 
Не заходите в соц. сети
Полезно поддерживать профессиональные аккаунты в актуальном состоянии. Но иногда это превращается в бездумный серфинг в интернете и растягивается на несколько часов.
Отчитывайтесь кому-то о дедлайнах
Например, договоритесь с другом или коллегой, что будете оповещать о выполнении какой-то задачи. Стыдно будет признаваться, что вы прокрастинировали и просрочили дедлайн, поэтому вы начнёте больше стараться. В наш коворкинг вы можете приходить с друзьями и даже не придется звонить или писать - вы можете показать результат вживую и спросить совета, если в чем-то неуверены.
Всегда имейте в запасе какую-то механическую работу
Иногда просто нет сил на сложные задачи, требующие творческого подхода или концентрации. На такие случаи составьте список необходимых, но скучных механических дел.
Планируйте отдых
Очень сложно расслабиться, когда рабочее место прямо под боком. Поэтому важно выделять в своём расписании перерывы на отдых. Например, в нашем пространстве есть оборудованная кухня с кофемашиной, куда вы можете отойти, чтобы сделать вкусный кофе и перекусить фруктами и полезными снеками и еще быстрее восстановить силы. 
Не отвлекайтесь
Когда вы находитемь дома, где за вами никто не следит, у вас может возникать желание отвлечься на что-то или на кого-то. И так вы не заметите, как пройдет час или два. В коворкинге Qubity Space вы будете находится в окружении работающих людей, глядя на которых вам не захочется прокрастинировать. А еще там нет домашних дел, а уборку выполняет клининг.
Обустройте рабочее место. 
Для продуктивной работы (и здоровой спины) нужен удобный стол и стул, достаточно света и свежего воздуха. Работать лежа в кровати, конечно, приятно, но до момента пока вас не будет постоянно клонить в сон. В нашем open-space вы можете разместиться как за столом на мягком кресле, так и на мягком диване и кресле мешке. А смена обстановки будет позитивно влиять на вашу бодрость и настроение.
Постоянно общайтесь с людьми
Личное общение трудно переоценить, даже если вы интроверт. Оно даёт новые идеи и просто помогает выбраться из собственного пузыря. В нашем бизнес-коворкинге может одновременно работать до 112 человек - среди них вы точно найдете единомышленника, а, возможно, и будущего друга или партнера.

Эти простые советы помогут  не только справляться с работой проще и быстрее, но и приобрести полезные привычки для вашей повседневной жизни.

В следующих сообщениях Вы получите больше информации о нашем коворинге.

P.S. Если при заполнении формы на сайте Вы по ошибке ввели неверный телефон или сомневаетесь в его правильности, Вы можете оставить номер еще раз прямо тут.

Отправьте Ваш номер телефона  пожалуйста...''')
        num_wait = await User.number2.set()
        await asyncio.sleep(86400)
        async with aiosqlite.connect("dbas1982324804:AAHbX1a1M_B-QCYDuoKZYu-717WJxtDOq2ce.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            #conn = await con.cursor()
            s = await con.execute("SELECT number FROM users WHERE id = ?;", (message.from_user.id, ))
            s = await s.fetchone()
        if not s.isdigit():
            await state.finish()
            await message.answer('''Ошибки коворкингов, которые учтены в Qubity Space

Удаленная работа из дома. В 2020 году все люди принудительно узнали, что это такое и ощутили на себе все плюсы и минусы remote work. И если по началу большинству людей нравилась работать дома,  то со временем они начали уставать от однообразия и монотонности. 
Неплохим решением для многих стали коворкинги – центры, в которых арендовать рабочее место может любой желающий.
Бизнесмены, стартаперы, фрилансеры и просто творческие люди поначалу оценили все плюсы работы в таком месте, но в какой-то момент резиденты подобных заведений понимают, что помещения перестают быть друзьями для их бизнеса. И вот почему:
Трудности при проведении встреч
Open-space не самое подходящее место для встречи с партнерами и клиентами. Согласитесь, не очень хочется, чтобы вокруг тебя находились “лишние уши”. Вашему приглашенному может быть неловко, к тому же, большинство считает такой формат встреч непрестижным.
Резиденты коворкинга Qubity Space могут бесплатно воспользоваться оборудованной переговорной с шумоизоляцией, где точно никто не подслушает и не будет мешать. Если у вас несколько встреч подряд и на предыдущей вы задержались или клиент приехал раньше, то наши приветливые администраторы встретят вашего гостя, проводят его в комнату отдыха, где он сможет комфортно подождать.
Шумный open-space
Посетители большинства коворкингов страдают от шума и невозможности сосредоточиться, когда вокруг много людей. 
В нашем пространстве действует система штрафов - если резидент ведет себя шумно и мешает остальным, администратор сделает ему замечание. За 3 замечания резидент попадает в черный список и не имеет права посещать коворкинг 1 месяц.
Нет гарантии безопасности
Посетить коворкинг может любой человек, который заплатил за аренду места.  Но поскольку на этих площадях часто обитают люди с улицы, степень безопасности личных вещей и идей сокращается. 
В Qubity Space каждый резидент имеет собственный локер, может зайти только по карте-ключу и Face ID, все пространство оборудовано камерами, а за порядком следят администраторы.
Несовпадение графиков
Многие коворкинги уже перешли на круглосуточный режим работы, но еще не везде вы можете поработать в любые часы, и приходится подстраиваться.
Если вы арендуете закрепленное место у нас, то вы можете прийти поработать в любое время суток, даже ночью.
Платная техника, кофе, снеки
Коворкинг - место для работы, отдохнуть и поесть можно дома, или, на крайний случай, в ближайшем кафе.
Мы там не считаем - резиденты Qubity Space вместе с удобным рабочим местом получают еще и неограниченный кофе, фрукты и снеки, бесплатно могут пользоваться любой офисной техникой.

В Qubity Space мы пострались развеять все мифы о работе в коворкингах и сделать пространство максимально комфортным для вашей продуктивности. Будем рады видеть вас в числе наших резидентов!''')
            await asyncio.sleep(86400)
            await message.answer('''Дизайнерский ремонт в современном стиле, панорамные окна, собственный спортзал и кухня - видеообзор пространства Qubity Space

Неважно, успели вы посетить наш коворкинг или еще нет, вы можете посмотреть, как выглядит наше пространство внутри в небольшом видео.
Будучи резидентом, вы сможете посещать все эти зоны и использовать все преимущества коворкинга.
Приятного просмотра!''')
            await asyncio.sleep(86400)
            await message.answer('''Почему работая в коворкинге ты намного быстрее станешь лучше как специалист и начнешь больше зарабатывать? - отзыв от резидента Qubity Space

Меня зовут Дмитрий, я занимаюсь созданием сайтов уже более 8 лет, 5 лет из которых я работаю на фрилансе. Изначально, когда ушел из офиса, работал дома или в кофейне неподалеку. Понял, что работа из дома дается мне нелегко - не могу сосредоточиться, а в кофейне шумно и не всегда есть место, где можно сесть.
Поэтому стал искать коворкинг в Москве, чтобы было удобно и недалеко от меня.
За пару лет поменял несколько мест, где-то нравилось больше, где-то меньше, но везде были свои недостатки. Для работы мне важна тишина, удобное рабочее место и круглосуточный доступ, т.к. иногда люблю зависнуть над проектом до 12 ночи. В большинстве коворкингов этого не хватало.
Пару месяцев назад друг посоветовал посетить коворкинг Qubity Space. Подкупило, что он находится недалеко от моего дома (15 минут пешком). Пришел на тестовый день и уже работаю там с июня. Это потрясающее место. Если судить по внешним факторам — это пожалуй лучшее место, что я встречал. Сразу как попадаешь сюда, интерьер очень подкупает. Внутри все очень красиво и аккуратно. Отличные удобные офисные кресла и столы. Еще мне особенно нравится то, что коворкинг расположен в бизнес-центре в окружении разных заведений и с развитой инфраструктурой. Есть большой выбор, куда сходить на обед. К тому же можно перекусить прямо в самом коворкинге - тут есть большая просторная кухня с бесплатным кофе. 
Что еще поразило - это абсолютная тишина, почти как в библиотеке. Штрафы за шум, конечно, жестко, зато дисциплина отличная. 
Здесь есть удобная выделенная переговорная с проектором, чего я не встречал в остальных коворкингах.
Еще огромный плюс в пользу Qubity Space - можно работать круглосуточно, если арендовать закрепленное место или офис. Никто в 20:00 не выгоняет, как было на моем предыдущем опыте.
Еще один момент, нельзя снимать коворкинг посуточно или на неделю. Только на месяц, по словам администраторов, этим ограничением они хотят избежать текучки людей и создать дружественную среду, где люди между собой знакомы. Что ж, цель хорошая.

В общем, это отличное место для работы, особенно если вы устали от “домашнего офиса”. Обстановка настраивает на рабочий лад.''')
            await asyncio.sleep(86400*3)
            media = types.MediaGroup()
            media.attach_photo("https://i.imgur.com/d2JHzX7.jpg")
            media.attach_photo("https://i.imgur.com/C1Nue4Q.jpg")
            media.attach_photo("https://i.imgur.com/9Zkuyo5.jpg", '''От чего зависит успех деловой встречи?Конечно же от обстановки!

Естественно важны и другие факторы, например, ваша подготовка, внешний вид, умение презентовать и договариваться. Но даже это все не поможет, если проводить переговоры в неподходящем месте.
Это мы учли в наших переговорных комнатах, ведь именно по обстановке зачастую партнеры или гости судят о солидности мероприятия в целом.

В комнате для переговоров имеется:
проектор
флип-чарт
стабильный быстрый Wi-Fi

🚪Арендуемая площадь - 18 кв.м.

🎎Зал вмещает до 10 человек, мебель стоит по принципу «Круглый стол», также по запросу возможна «театральная» расстановка кресел.

☕️Для комфортного проведения деловых мероприятий у вас будет неограниченный доступ к напиткам, фруктам и снекам. Также в перерыве вы можете разместиться в удобной конмнате отдыха и передохнуть.

Каждый резидент с закрепленным рабочим местом получает доступ к переговорной совершенно бесплатно и может забранировать ее от 1 ч в день.''')
            await message.bot.send_media_group(message.chat.id, media=media)
            await asyncio.sleep(86400*3)
            await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
            await asyncio.sleep(86400*3)
            await message.answer('''Какое время работы локаций и есть ли парковка - ответили на самые популярные вопросы о коворкинге Qubity Space 

Можно ли приводить гостей, если у меня самого тестовый день? А прийти на него второй раз в другую локацию?
Пробный день в коворкинге создан для того, чтобы вы могли прочувствовать атмосферу работы в Qubity Space. Если вы уже побывали в одной из локаций и хотите поработать в течение дня в другой, обратите внимание на тариф “Гость”. Если вам необходимо провести встречу, рекомендуем рассмотреть возможность аренды переговорных комнат или также воспользоваться тарифом “Гость”, включающим посещение 1 гостя.
Где можно припарковаться? 
В Qubity Space обратите внимание на подземную парковку или наземную парковку БЦ “Нео Гео”. Позвоните администратору коворкинга заранее, чтобы узнать, доступно ли парковочное место в запланированное вами время посещения коворкинга. Также на срок от 1 месяца возможно арендовать парковочное место в БЦ.
У вас в офисах есть мебель? Можно ли привезти свою? 
Каждый офис Qubity Space оборудован столами и креслами в соответствии с количеством рабочих мест в нем. Обустроить кабинет вы можете на своё усмотрение (только не забудьте предварительно оповестить администратора, если вы собираетесь вносить в коворкинг что-то крупногабаритное). Если мы получаем от резидентов большое количество запросов на какой-то определённый тип мебели (например, тумбы), рассматриваем возможность дополнить обустройство рабочих мест. Также мы предоставляем в аренду персональные локеры.
Время работы локаций? 
Для резидентов, выбравших тариф "Резидент" или Smart-офис коворкинг открыт круглосуточно. Для резидентов коворкинга, выбравших тариф “Гость”, – с 8:00 до 20:00, в рабочее время команды локации.
Как осуществляется охрана коворкинга? 
Вход в коворкинг осуществляется строго по пропускам резидентов и Face-ID. Также в офисных пространствах установлены камеры видеонаблюдения, к записям с которых в случае необходимости мы можем обратиться. Каждый резидент получает собственный локер для хранения личных вещей, а за порядком следят администраторы.
Вы предоставляете юридический адрес?
Юридический адрес является дополнительной услугой и предоставляется только арендаторам кабинетов, выбравшим срок аренды от 11 месяцев, а также арендой от 25 мест. Вначале мы заключаем с вами договор субаренды, затем вы оплачиваете услугу, и мы готовим подтверждающие вашу работу в офисном пространстве документы для налоговой.
Как организовать мероприятие на вашей площадке? 
Если вы уже определились с датой, ознакомьтесь со свободными временными окнами у администраторов пространства. Если дата свободна, можно приступать к обсуждению деталей события: какое техническое оснащение для него потребуются, какой формат рассадки предполагается, какое количество гостей вы ожидаете увидеть. Во всех наших локациях действует пропускная система, поэтому не забудьте при регистрации запросить у гостей их полные ФИО.

Если у вас остались вопросы, то вы можете задать их администраторам коворкинга Qubity, написав боту в ответ на это сообщение или по телефону: +7 (926) 911-13-96.''')
            q = await User.question.set()
            await asyncio.sleep(86400*3)
            if not q:
                await message.answer('''Что можно купить за 450 Р? 2 чашки кофе или 1 день в современном коворкинге Qubity Space и пить кофе в неограниченном количестве

Стоимость размещения в коворкинге зависит от того, арендуете вы незакрепленное место в open space или закрепленное в офисе, а также от времени доступа в коворкинг. 

Наши тарифы:

Гость - 1000 Р/день
Незакрепленное место в openspace
Доступ 1 день (8:00-20:00)
Кофе-брейки
Лаундж-зона (30 мин.)
Skype-room (30 мин.)
Все общие зоны

Резидент Light - 14.500 Р/месяц
Незакрепленное место в openspace
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Резидент Platinum - 18.500 Р/месяц
Закрепленное место в Smart-офисе
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Smart-офис - от 16.000 Р/чел
Индивидуальный Smart-офис
Доступ 24/7
Кофе-брейки
Лаундж-зона (от 1 ч./день)
Skype-room (от 1 ч./день)
Все общие зоны

Приходите на бесплатный день в коворкинге Qubity Space, чтобы подобрать тариф для себя
Переходите по ссылке на наш сайт, чтобы забронировать бесплатное место в коворкинге: http://qubity.space/''')
                await state.finish()
    

@dp.message_handler(state=User.number2, content_types="text")
async def numbergetting(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        if 12 >= len(list(message.text)) >= 9:
            try:
                async with aiosqlite.connect("dbase.db") as con:
                    conn = await con.cursor()
                    await conn.execute("INSERT INTO users VALUES(?,?,?,?,?,?,?,?,?);", (message.from_user.id, message.from_user.first_name, str(f"{message.text}"), "Без вопросов получил бонус", "Не отвечал на вопросы", "Без вопросов получил бонус", "Не отвечал на вопросы", "Без вопросов получил бонус", "Не отвечал на вопросы", ))
                    await con.commit()
            except sqlite3.IntegrityError as e:
                print(e)
                async with aiosqlite.connect("dbase.db") as con:
                    conn = await con.cursor()
                    await conn.execute("UPDATE users SET number = ? WHERE id = ?;", (str(message.text), message.from_user.id, ))
                    await con.commit()
            await bot.send_message(admin_id, f"Имя: <b>{message.from_user.first_name}</b> \nID: <code>{message.from_user.id}</code> \nЮзернэйм: <code>@{message.from_user.username}</code> \nНомер: <code>{message.text}</code> \n\n<a href='tg://openmessage?user_id={message.from_user.id}'>Перейти к пользователю</a>".replace("@None", "Отсутствует"))
            await message.answer("<b>Спасибо, мы приняли Ваши контактные данные.</b> \n\nСовсем скоро с вами свяжется наш администратор, уточнит детали вашего визита и ответит на ваши вопросы.")
            await asyncio.sleep(86400)
            await message.answer('''Ошибки коворкингов, которые учтены в Qubity Space

Удаленная работа из дома. В 2020 году все люди принудительно узнали, что это такое и ощутили на себе все плюсы и минусы remote work. И если по началу большинству людей нравилась работать дома,  то со временем они начали уставать от однообразия и монотонности. 
Неплохим решением для многих стали коворкинги – центры, в которых арендовать рабочее место может любой желающий.
Бизнесмены, стартаперы, фрилансеры и просто творческие люди поначалу оценили все плюсы работы в таком месте, но в какой-то момент резиденты подобных заведений понимают, что помещения перестают быть друзьями для их бизнеса. И вот почему:
Трудности при проведении встреч
Open-space не самое подходящее место для встречи с партнерами и клиентами. Согласитесь, не очень хочется, чтобы вокруг тебя находились “лишние уши”. Вашему приглашенному может быть неловко, к тому же, большинство считает такой формат встреч непрестижным.
Резиденты коворкинга Qubity Space могут бесплатно воспользоваться оборудованной переговорной с шумоизоляцией, где точно никто не подслушает и не будет мешать. Если у вас несколько встреч подряд и на предыдущей вы задержались или клиент приехал раньше, то наши приветливые администраторы встретят вашего гостя, проводят его в комнату отдыха, где он сможет комфортно подождать.
Шумный open-space
Посетители большинства коворкингов страдают от шума и невозможности сосредоточиться, когда вокруг много людей. 
В нашем пространстве действует система штрафов - если резидент ведет себя шумно и мешает остальным, администратор сделает ему замечание. За 3 замечания резидент попадает в черный список и не имеет права посещать коворкинг 1 месяц.
Нет гарантии безопасности
Посетить коворкинг может любой человек, который заплатил за аренду места.  Но поскольку на этих площадях часто обитают люди с улицы, степень безопасности личных вещей и идей сокращается. 
В Qubity Space каждый резидент имеет собственный локер, может зайти только по карте-ключу и Face ID, все пространство оборудовано камерами, а за порядком следят администраторы.
Несовпадение графиков
Многие коворкинги уже перешли на круглосуточный режим работы, но еще не везде вы можете поработать в любые часы, и приходится подстраиваться.
Если вы арендуете закрепленное место у нас, то вы можете прийти поработать в любое время суток, даже ночью.
Платная техника, кофе, снеки
Коворкинг - место для работы, отдохнуть и поесть можно дома, или, на крайний случай, в ближайшем кафе.
Мы там не считаем - резиденты Qubity Space вместе с удобным рабочим местом получают еще и неограниченный кофе, фрукты и снеки, бесплатно могут пользоваться любой офисной техникой.

В Qubity Space мы пострались развеять все мифы о работе в коворкингах и сделать пространство максимально комфортным для вашей продуктивности. Будем рады видеть вас в числе наших резидентов!''')
            await asyncio.sleep(86400)
            await message.answer('''Дизайнерский ремонт в современном стиле, панорамные окна, собственный спортзал и кухня - видеообзор пространства Qubity Space

Неважно, успели вы посетить наш коворкинг или еще нет, вы можете посмотреть, как выглядит наше пространство внутри в небольшом видео.
Будучи резидентом, вы сможете посещать все эти зоны и использовать все преимущества коворкинга.
Приятного просмотра!''')
            await asyncio.sleep(86400)
            await message.answer('''Почему работая в коворкинге ты намного быстрее станешь лучше как специалист и начнешь больше зарабатывать? - отзыв от резидента Qubity Space

Меня зовут Дмитрий, я занимаюсь созданием сайтов уже более 8 лет, 5 лет из которых я работаю на фрилансе. Изначально, когда ушел из офиса, работал дома или в кофейне неподалеку. Понял, что работа из дома дается мне нелегко - не могу сосредоточиться, а в кофейне шумно и не всегда есть место, где можно сесть.
Поэтому стал искать коворкинг в Москве, чтобы было удобно и недалеко от меня.
За пару лет поменял несколько мест, где-то нравилось больше, где-то меньше, но везде были свои недостатки. Для работы мне важна тишина, удобное рабочее место и круглосуточный доступ, т.к. иногда люблю зависнуть над проектом до 12 ночи. В большинстве коворкингов этого не хватало.
Пару месяцев назад друг посоветовал посетить коворкинг Qubity Space. Подкупило, что он находится недалеко от моего дома (15 минут пешком). Пришел на тестовый день и уже работаю там с июня. Это потрясающее место. Если судить по внешним факторам — это пожалуй лучшее место, что я встречал. Сразу как попадаешь сюда, интерьер очень подкупает. Внутри все очень красиво и аккуратно. Отличные удобные офисные кресла и столы. Еще мне особенно нравится то, что коворкинг расположен в бизнес-центре в окружении разных заведений и с развитой инфраструктурой. Есть большой выбор, куда сходить на обед. К тому же можно перекусить прямо в самом коворкинге - тут есть большая просторная кухня с бесплатным кофе. 
Что еще поразило - это абсолютная тишина, почти как в библиотеке. Штрафы за шум, конечно, жестко, зато дисциплина отличная. 
Здесь есть удобная выделенная переговорная с проектором, чего я не встречал в остальных коворкингах.
Еще огромный плюс в пользу Qubity Space - можно работать круглосуточно, если арендовать закрепленное место или офис. Никто в 20:00 не выгоняет, как было на моем предыдущем опыте.
Еще один момент, нельзя снимать коворкинг посуточно или на неделю. Только на месяц, по словам администраторов, этим ограничением они хотят избежать текучки людей и создать дружественную среду, где люди между собой знакомы. Что ж, цель хорошая.

В общем, это отличное место для работы, особенно если вы устали от “домашнего офиса”. Обстановка настраивает на рабочий лад.''')
            await asyncio.sleep(86400*3)
            media = types.MediaGroup()
            media.attach_photo("https://i.imgur.com/d2JHzX7.jpg")
            media.attach_photo("https://i.imgur.com/C1Nue4Q.jpg")
            media.attach_photo("https://i.imgur.com/9Zkuyo5.jpg", '''От чего зависит успех деловой встречи?Конечно же от обстановки!

Естественно важны и другие факторы, например, ваша подготовка, внешний вид, умение презентовать и договариваться. Но даже это все не поможет, если проводить переговоры в неподходящем месте.
Это мы учли в наших переговорных комнатах, ведь именно по обстановке зачастую партнеры или гости судят о солидности мероприятия в целом.

В комнате для переговоров имеется:
проектор
флип-чарт
стабильный быстрый Wi-Fi

🚪Арендуемая площадь - 18 кв.м.

🎎Зал вмещает до 10 человек, мебель стоит по принципу «Круглый стол», также по запросу возможна «театральная» расстановка кресел.

☕️Для комфортного проведения деловых мероприятий у вас будет неограниченный доступ к напиткам, фруктам и снекам. Также в перерыве вы можете разместиться в удобной конмнате отдыха и передохнуть.

Каждый резидент с закрепленным рабочим местом получает доступ к переговорной совершенно бесплатно и может забранировать ее от 1 ч в день.''')
            await message.bot.send_media_group(message.chat.id, media=media)
            await asyncio.sleep(86400*3)
            await message.answer('''Офис vs open space. В каких условиях лучше работать?

Привычные кабинеты, как в гос. учреждениях, сегодня уходят на второй план. Все больше людей выбирает работу в open space - больших помещениях с рабочими местами. И, казалось бы, что тут такого — все вместе, рядом, больше общения, проще решать рабочие вопросы. Но многим такой формат организации рабочего пространства не подходит, поэтому они выбирают изолированные офисы. Давайте разберемся, какие преимущества есть у open space и кабинетов.

Плюсы open space
Повышение продуктивности. Когда много людей работают в одном помещении, они ненарочно настраивают друг друга на рабочий лад. Вы не будете прократинировать и отвлекаться от работы видя, как работают другие.
Возможность выбрать себе место. Если вы арендуете незакрепленное место в коворкинге, то можете каждый день или даже час менять обстановку. Это приносит разнообразие в рабочую жизнь, нежели вы бы видели перед глазами одну и ту же картину.
Постоянное общение. В open space может работать много людей одновременно - хотя бы один из них точно будет специалистом из вашей сферы. Так вы будете находится в одном пространстве, можете познакомиться, обсудить проекты и дать друг другу парочку советов.

Плюсы офисов
Уединенность. Если вы не можете сосредоточиться, когда вокруг вас много людей или ваша работа подразумевает полное уединение, то лучше выбрать изолированный офис. Здесь вы будете находиться в полной тишине и никто не будет отвлекать вас от работы.
Обустройство рабочего места. В свой офис вы можете принести любую технику и личные вещи, которые нужны вам для работы. Вы можете подстроить пространство под себя и не носить каждый раз вещи домой и обратно.
Нет ограничения личной свободы. В open space принято не шуметь, не разговаривать по телефону, переводить все гаджеты на беззвучный режим. В своем кабинете свободы больше, главное, установить общие правила с коллегами.

В нашем пространстве Qubity Space есть и тихий open space, и изолированные офисы. Вы сами можете выбрать, где вам удобнее и приятнее работать. На бесплатном тестовом дне можно попробовать оба варианта и решить, где вам понравилось больше.
Ждем вас в кругу резидентов Qubity Space!''')
            await asyncio.sleep(86400*3)
            await message.answer('''Какое время работы локаций и есть ли парковка - ответили на самые популярные вопросы о коворкинге Qubity Space 

Можно ли приводить гостей, если у меня самого тестовый день? А прийти на него второй раз в другую локацию?
Пробный день в коворкинге создан для того, чтобы вы могли прочувствовать атмосферу работы в Qubity Space. Если вы уже побывали в одной из локаций и хотите поработать в течение дня в другой, обратите внимание на тариф “Гость”. Если вам необходимо провести встречу, рекомендуем рассмотреть возможность аренды переговорных комнат или также воспользоваться тарифом “Гость”, включающим посещение 1 гостя.
Где можно припарковаться? 
В Qubity Space обратите внимание на подземную парковку или наземную парковку БЦ “Нео Гео”. Позвоните администратору коворкинга заранее, чтобы узнать, доступно ли парковочное место в запланированное вами время посещения коворкинга. Также на срок от 1 месяца возможно арендовать парковочное место в БЦ.
У вас в офисах есть мебель? Можно ли привезти свою? 
Каждый офис Qubity Space оборудован столами и креслами в соответствии с количеством рабочих мест в нем. Обустроить кабинет вы можете на своё усмотрение (только не забудьте предварительно оповестить администратора, если вы собираетесь вносить в коворкинг что-то крупногабаритное). Если мы получаем от резидентов большое количество запросов на какой-то определённый тип мебели (например, тумбы), рассматриваем возможность дополнить обустройство рабочих мест. Также мы предоставляем в аренду персональные локеры.
Время работы локаций? 
Для резидентов, выбравших тариф "Резидент" или Smart-офис коворкинг открыт круглосуточно. Для резидентов коворкинга, выбравших тариф “Гость”, – с 8:00 до 20:00, в рабочее время команды локации.
Как осуществляется охрана коворкинга? 
Вход в коворкинг осуществляется строго по пропускам резидентов и Face-ID. Также в офисных пространствах установлены камеры видеонаблюдения, к записям с которых в случае необходимости мы можем обратиться. Каждый резидент получает собственный локер для хранения личных вещей, а за порядком следят администраторы.
Вы предоставляете юридический адрес?
Юридический адрес является дополнительной услугой и предоставляется только арендаторам кабинетов, выбравшим срок аренды от 11 месяцев, а также арендой от 25 мест. Вначале мы заключаем с вами договор субаренды, затем вы оплачиваете услугу, и мы готовим подтверждающие вашу работу в офисном пространстве документы для налоговой.
Как организовать мероприятие на вашей площадке? 
Если вы уже определились с датой, ознакомьтесь со свободными временными окнами у администраторов пространства. Если дата свободна, можно приступать к обсуждению деталей события: какое техническое оснащение для него потребуются, какой формат рассадки предполагается, какое количество гостей вы ожидаете увидеть. Во всех наших локациях действует пропускная система, поэтому не забудьте при регистрации запросить у гостей их полные ФИО.

Если у вас остались вопросы, то вы можете задать их администраторам коворкинга Qubity, написав боту в ответ на это сообщение или по телефону: +7 (926) 911-13-96.''')
            q = await User.question.set()
            await asyncio.sleep(86400*3)
            if not q:
                await message.answer('''Что можно купить за 450 Р? 2 чашки кофе или 1 день в современном коворкинге Qubity Space и пить кофе в неограниченном количестве

Стоимость размещения в коворкинге зависит от того, арендуете вы незакрепленное место в open space или закрепленное в офисе, а также от времени доступа в коворкинг. 

Наши тарифы:

Гость - 1000 Р/день
Незакрепленное место в openspace
Доступ 1 день (8:00-20:00)
Кофе-брейки
Лаундж-зона (30 мин.)
Skype-room (30 мин.)
Все общие зоны

Резидент Light - 14.500 Р/месяц
Незакрепленное место в openspace
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Резидент Platinum - 18.500 Р/месяц
Закрепленное место в Smart-офисе
Доступ 24/7
Кофе-брейки
Лаундж-зона (1 ч./день)
Skype-room (1 ч./день)
Все общие зоны

Smart-офис - от 16.000 Р/чел
Индивидуальный Smart-офис
Доступ 24/7
Кофе-брейки
Лаундж-зона (от 1 ч./день)
Skype-room (от 1 ч./день)
Все общие зоны

Приходите на бесплатный день в коворкинге Qubity Space, чтобы подобрать тариф для себя
Переходите по ссылке на наш сайт, чтобы забронировать бесплатное место в коворкинге: http://qubity.space/''')
                await state.finish()
        else:
            await message.reply("Номер состоит из 9-12 чисел \nОтправьте Ваш номер(в формате: 79083080269) заново...")
            await User.number2.set()
    else:
        await message.reply(f'Отправьте мне свой номер телефона(в формате: 79083080269) \n\nЖду Ваш номер:')
        await User.number2.set()
  

@dp.message_handler(commands=["help"])
async def helping(message):
    
    await message.reply("<i>Команды:</i> \n - /start : <b>Начать опрос/бота</b> \n - /help : <b>Посмотреть команды</b> \n - /change - <b>Перепройти опрос</b>")


@dp.message_handler(commands=["change"])
async def changing(message):
    await message.answer("Сколько Вас будет?", reply_markup=Buttons2.question_1())


@dp.message_handler(state=User.number4, content_types=["text"])
async def changeinfo(message):
    async with aiosqlite.connect('dbase.db') as con:
        conn = await con.cursor()
        await conn.execute('UPDATE users SET number = ? WHERE id = ?', (str(f'{message.text}'), message.from_user.id, ))
        await con.commit()
        info = await conn.execute('SELECT * FROM users WHERE id = ?', (message.from_user.id, ))
        info = await info.fetchall()
    beh = str(info[0]).replace("(", "").replace(")", "").replace("'", "").split(", ")
    await bot.send_message(chat_id=admin_id, text=f'<a href="tg://openmessage?user_id={message.from_user.id}">{message.from_user.first_name}({message.from_user.id})</a> сменил свои данные на новые! \nЧто это значит? \n - Данный пользователь перепрошел опрос и ввел новый номер телефона! \n\n<b>Время записан в часовом поясе Екатеринбурга(+5)!</b> \nИмя: <code>{message.from_user.first_name}</code> \nФамилия: <code>{message.from_user.last_name}</code> \nНомер: <code>{beh[2]}</code> \nID пользователя: <code>{message.from_user.id}</code> \nЮзернэйм пользователя: <code>@{message.from_user.username}</code> \n\nИнформация о действиях пользователя: \n - Ответ на первый опрос: <b>{beh[3]}</b> \n - Время ответа на первый опрос: <b>{beh[4]} | {beh[5]}</b> \n\n - Ответ на второй опрос: <b>{beh[6]}</b> \n - Время ответа на второй опрос: <b>{beh[7]} | {beh[8]}</b> \n\n - Ответ на третий опрос: <b>{beh[9]}</b> \n - Время ответа на третий опрос: <b>{beh[10]} | {beh[11]}</b> \n\n\n<a href="tg://openmessage?user_id={message.from_user.id}">Перейти к пользователю</a>'.replace("@None", "Отсутствует"), disable_notification=True)
    await message.answer("Ваши данные обновлены успешно!")
    await state.finish()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot_info())
    executor.start_polling(dp, skip_updates=True)
