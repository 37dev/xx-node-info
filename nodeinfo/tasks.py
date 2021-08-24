import json

import telegram
from celery.signals import worker_ready
from django.conf import settings
from telegram.utils.helpers import escape_markdown

from clients.xx_sse_client import XxSSEClient
from dtb.celery import app
from nodeinfo.models import NodeInfo
from tgbot.handlers.dispatcher import bot
from tgbot.utils import get_node_status_info_text


@app.task(ignore_result=True)
@worker_ready.connect
def xx_sse_nodes_uptime_info_consumer(sender, **kwargs):
    client = XxSSEClient(settings.XX_SSE_URL)

    for event in client.events():
        if event.event == "node_statuses_updated":
            data = json.loads(event.data)
            NodeInfo.objects.update_or_create_from_event_data(data)


@app.task(ignore_result=True)
def users_node_uptime_notifier(**kwargs):
    node_info_pk = kwargs["node_info_pk"]
    node_status = kwargs["node_status"]

    node = NodeInfo.objects.get(pk=node_info_pk)

    for user in node.subscribed_users.all():
        bot.send_message(
            text=escape_markdown(
                get_node_status_info_text(
                    node_status, node.node_id
                ),
                version=2
            ),
            chat_id=user.user_id,
            parse_mode=telegram.ParseMode.MARKDOWN_V2
        )
