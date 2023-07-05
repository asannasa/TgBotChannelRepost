import logging
import config as cfg
from telethon import TelegramClient, events

logging.basicConfig(filename='TgBot.log', encoding='utf-8', level=logging.INFO)
client = TelegramClient('session_name', cfg.api_id, cfg.api_hash)


@client.on(events.Album(chats=cfg.channel_id))
async def handler_snd(event):
    for chat_id_n in cfg.chats_id:
        try:
            await client.forward_messages(chat_id_n, event.messages)
        except ValueError as err:
            logging.warning(err)


@client.on(events.NewMessage(chats=cfg.channel_id))
async def normal_handler(event):
    if not event.grouped_id:
        for chat_id_n in cfg.chats_id:
            try:
                await client.forward_messages(chat_id_n, event.message)
            except ValueError as err:
                logging.warning(err)


if __name__ == '__main__':
    client.start(bot_token=cfg.bot_token)
    client.run_until_disconnected()
