import asyncio
import datetime
import logging
import config
from aiogram import Bot, Dispatcher, executor, types
from database.birth_days import dict_days
from get_users.get_users import get_channel_users

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.token)
dp = Dispatcher(bot)

my_telegram_id = 123123123213


@dp.message_handler(commands=['user_list'])
async def echo_msg(msg: types.Message):
    chanel_users = await get_channel_users(bot_token=config.token, chat_id=config.chat_id)
    names = []
    for user in chanel_users:
        name = user.user.first_name
        names.append(name)
        print(name)
    await msg.reply(names)


@dp.message_handler()
async def echo_msg_pm(msg: types.Message):
    chat_id = msg.chat.id.__str__()
    chat_name = msg.chat.full_name
    text = msg.text
    # await bot.send_message(chat_id=my_telegram_id, text=chat_id)
    await bot.send_message(chat_id=my_telegram_id, text='{id} - {chat_name} - {text}'.format(id=chat_id, chat_name=chat_name, text=text))


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
        await asyncio.sleep(3)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(reminder())
    executor.start_polling(dp, skip_updates=True)
