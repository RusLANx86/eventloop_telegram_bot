from pyrogram import Client, filters


async def get_channel_users(bot_token, chat_id):
    chanel_users = []
    app = Client(
        api_id=123124234,
        api_hash='85675erygegf324',
        session_name="my_bot",
        bot_token=bot_token
    )
    await app.start()

    members = app.iter_chat_members(chat_id=chat_id)
    async for member in members:
        chanel_users.append(member)

    await app.stop()

    return chanel_users
