import config as cfg
from telethon import TelegramClient, events


client = TelegramClient('session_name', cfg.api_id, cfg.api_hash)


@client.on(events.NewMessage(chats=cfg.channel_id))
async def normal_handler(event):
    try:
        with open("chat_id.txt", "r") as chat_f:
            for chat_id_f in chat_f:
                try:
                    await client.forward_messages(int(chat_id_f), event.message)
                except ValueError as err:
                    print(err)
    except IOError:
        print('File no')


if __name__ == '__main__':
    client.start(bot_token=cfg.bot_token)
    client.run_until_disconnected()
