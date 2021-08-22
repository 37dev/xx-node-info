import telegram

from dtb.celery import app
from celery.utils.log import get_task_logger

from tgbot.handlers.dispatcher import bot, dispatcher

logger = get_task_logger(__name__)


@app.task(ignore_result=True)
def process_telegram_event(update_json):
    update = telegram.Update.de_json(update_json, bot)
    dispatcher.process_update(update)
