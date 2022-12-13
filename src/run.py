import asyncio
import datetime
import logging
from uuid import uuid4
from datetime import datetime as dt

import config
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import link
from database.birth_days import dict_days
from get_users.framework_pyrogram import get_channel_users

from database import database as db


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.token)
dp = Dispatcher(bot)

my_telegram_id = 0


@dp.message_handler(commands=['user_list'])
async def echo_msg(msg: types.Message):
    chanel_users = await get_channel_users(bot_token=config.token, chat_id=config.chat_id)
    names = []
    for user in chanel_users:
        name = user.user.first_name
        names.append(name)
        print(name)
    await msg.reply(names)


@dp.message_handler(commands=['Катушка'])
async def create_katushka(msg: types.Message):
    customer = msg.from_user
    id_katushka = uuid4()
    text = link('Перейдите по ссылке! =)', f'192.168.128.11:5000/race/{id_katushka}')

    bike_ride = db.BikeRides()
    bike_ride.uid = str(id_katushka)
    bike_ride.creator = customer.full_name
    bike_ride.ride_datetime = str(dt.utcnow().replace(second=0, microsecond=0))
    bike_ride.meet_time = str(dt.now().time().replace(second=0, microsecond=0))

    db.session.add(bike_ride)
    db.session.commit()

    await msg.reply(text=text)
    # await msg.reply(text=f'[\<{customer.first_name}, Перейдите по ссылке\>](\<192.168.128.11:5000\>)', parse_mode='MarkdownV2')


@dp.message_handler(commands=['анкета'])
async def user_info(msg: types.Message):
    chat_id = msg.chat.id.__str__()
    chat_name = msg.chat.full_name
    await msg.reply(text='Введите свое имя')


@dp.message_handler()
async def echo_msg_pm(msg: types.Message):
    chat_id = msg.chat.id.__str__()
    thread_id = msg.message_thread_id  # ID топика
    chat_name = msg.chat.full_name
    text = msg.text
    # await bot.send_message(chat_id=my_telegram_id, text=chat_id)
    await bot.send_message(
        message_thread_id=thread_id,
        chat_id=chat_id,
        text='{id} - {chat_name} - {text}'.format(id=chat_id, chat_name=chat_name, text=text)
    )


async def reminder():
    birth_datay = dict_days
    while True:
        # await bot.send_message(chat_id=-769218299, text='Я робот')
        today = datetime.datetime.now()
        date = today.strftime('%d.%m')
        time = today.strftime('%H:%M:%S')
        hours = int(today.strftime('%H'))
        people = []
        for FIO, birthday in birth_datay.items():
            if date == birthday:
                people.append(FIO)
        if len(people) > 0 and hours in list(range(17, 22)):
            text = 'Сегодня День Рождения у: \n'
            print(text)
            for man in people:
                text = text + man + '\n'
                print(man)
            await bot.send_message(chat_id=config.chat_id, text=text)
        # await asyncio.sleep(3600*(9+(24-hours))) #Подсчет секунд до 9 утра следущего дня
        await asyncio.sleep(60000)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(reminder())

    from flask_app import run_app
    from threading import Thread

    t = Thread(target=run_app, args={"__name__": __name__})
    t.start()

    executor.start_polling(dp, skip_updates=True)
