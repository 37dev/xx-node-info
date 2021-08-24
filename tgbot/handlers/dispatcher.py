"""
    Telegram event handlers
"""

import telegram
from telegram.ext import (
    Dispatcher, CommandHandler
)

from dtb.settings import WEBHOOK_PORT, WEBHOOK_HOST, WEBHOOK_SECRET_ENDPOINT, TELEGRAM_TOKEN, CERT_PATH

from tgbot.handlers import commands


def setup_dispatcher():
    bot_instance = telegram.Bot(TELEGRAM_TOKEN)
    dispatcher_instance = Dispatcher(bot_instance, None, workers=0, use_context=True)

    dispatcher_instance.add_handler(CommandHandler("start", commands.command_start))
    dispatcher_instance.add_handler(CommandHandler("subscribe", commands.command_subscribe))
    dispatcher_instance.add_handler(CommandHandler("unsubscribe", commands.command_unsubscribe))

    bot_instance.setWebhook(url="{}:{}/{}".format(
        WEBHOOK_HOST,
        WEBHOOK_PORT,
        WEBHOOK_SECRET_ENDPOINT
    ), certificate=open(CERT_PATH, 'rb'))

    return dispatcher_instance, bot_instance


dispatcher, bot = setup_dispatcher()
