from aiogram import Dispatcher, executor, Bot
from aiogram import types
import asyncio
import config
from get_users.framework_pyrogram import get_channel_users

dp = Dispatcher(Bot(token=config.token))


async def background_on_start() -> None:
    """background task which is created when bot starts"""
    while True:
        await asyncio.sleep(5)
        print("Hello World!")


@dp.message_handler()
async def echo_msg(msg: types.Message):
    chanel_users = await get_channel_users(bot_token=config.token)
    names = []
    for user in chanel_users:
        name = user.user.first_name
        names.append(name)
        print(name)
    await msg.reply(names)


async def background_on_action() -> None:
    """background task which is created when user asked"""
    for _ in range(20):
        await asyncio.sleep(3)
        print("Action!")


async def background_task_creator(message: types.Message) -> None:
    """Creates background tasks"""
    asyncio.create_task(background_on_action())
    await message.reply("Another one background task create")


async def on_bot_start_up(dispatcher: Dispatcher) -> None:
    """List of actions which should be done before bot start"""
    asyncio.create_task(background_on_start())  # creates background task


"""Creates and starts the bot"""

# bot endpoints block:
dp.register_message_handler(
    background_task_creator,
    commands=['start']
)
# start bot
executor.start_polling(dp, skip_updates=True, on_startup=on_bot_start_up)
