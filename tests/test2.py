import sys
from getpass import getpass
from time import sleep

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import UsernameNotOccupiedError
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.types import ChannelParticipantsSearch, InputChannel

# First you need create app on https://my.telegram.org

phone = ''
limit = 100
api_id = 0
api_hash = ''


async def get_chat_info(username, client):
    try:
        chat = await client(ResolveUsernameRequest(username))
    except UsernameNotOccupiedError:
        print('Chat/channel not found!')
        sys.exit()
    result = {
        'chat_id': chat.peer.channel_id,
        'access_hash': chat.chats[0].access_hash
    }
    return result


def dump_users(chat, client):
    counter = 0
    offset = 0
    chat_object = InputChannel(chat['chat_id'], chat['access_hash'])
    all_participants = []
    print('Process...')
    while True:
        participants = client.invoke(GetParticipantsRequest(
            chat_object, ChannelParticipantsSearch(''), offset, limit
        ))
        if not participants.users:
            break
        all_participants.extend(['{} {}'.format(x.id, x.username)
                                 for x in participants.users])
        users_count = len(participants.users)
        offset += users_count
        counter += users_count
        print('{} users collected'.format(counter))
        sleep(2)
    with open('users.txt', 'w') as file:
        file.write('\n'.join(map(str, all_participants)))


channel_name = 'test_group_bot'
client = TelegramClient('current-session', api_id, api_hash)
print('Connecting...')
client.connect()
dump_users(get_chat_info(channel_name, client), client)
print('Done!')
