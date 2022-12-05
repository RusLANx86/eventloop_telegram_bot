import asyncio

from telethon.sync import TelegramClient
from telethon.tl.types import InputChannel
from telethon.tl.functions.contacts import ResolveUsernameRequest

import configparser
import json


async def get_group_members_info():
    api_id = 123
    api_hash = ''
    username = 'username_session'
    phone = '+1234567890'
    channel_href = 'https://t.me/+werwerwer'
    chat_id = '-1123123123'

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
