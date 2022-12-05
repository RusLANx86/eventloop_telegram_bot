import asyncio

from telethon.sync import TelegramClient
from telethon.tl.types import InputChannel
from telethon.tl.functions.contacts import ResolveUsernameRequest

import configparser
import json


async def get_group_members_info():
    api_id = 17367814
    api_hash = '941cb8f28ab6fc9c46b4bc9b988f6680'
    username = 'orpo_session'
    phone = '+9276869838'
    channel_href = 'https://t.me/+y1VuWHdQildkYmUy'
    chat_id = '-769218299'

    client = TelegramClient('orpo_session', api_id=api_id, api_hash=api_hash)
    client.start()
    await client.connect()

    dialogs = client.iter_dialogs()
    async for dialog in dialogs:
        print(dialog)

    channel = await client.get_entity('test_group_bot')

    members_telethon_list = await client.get_participants(channel, aggressive=True)

    username_list = [member.username for member in members_telethon_list]
    first_name_list = [member.first_name for member in members_telethon_list]
    last_name_list = [member.last_name for member in members_telethon_list]
    phone_list = [member.phone for member in members_telethon_list]
    print(username_list)
    return username_list, first_name_list, last_name_list, phone_list

loop = asyncio.get_event_loop()
loop.run_until_complete(get_group_members_info())
