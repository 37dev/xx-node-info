import json
import logging

import telegram
from celery.signals import worker_ready
from django.conf import settings
from telegram.utils.helpers import escape_markdown

from clients.xx_sse_client import XxSSEClient
from dtb.celery import app
from nodeinfo.models import NodeInfo
from tgbot.handlers.dispatcher import bot
from tgbot.utils import get_node_status_info_text


logger = logging.getLogger(__name__)


@worker_ready.connect
def at_worker_ready(sender, **k):
    with sender.app.connection() as conn:
        sender.app.send_task('nodeinfo.tasks.canary_xx_sse_nodes_uptime_info_consumer', connection=conn)
        sender.app.send_task('nodeinfo.tasks.mainnet_xx_sse_nodes_uptime_info_consumer', connection=conn)


@app.task(ignore_result=True)
def canary_xx_sse_nodes_uptime_info_consumer(**kwargs):
    while True:
        try:
            client = XxSSEClient(settings.XX_SSE_URLS["CANARY"])
            for event in client.events():
                if event.event == "node_statuses_updated":
                    data = json.loads(event.data)
                    NodeInfo.objects.update_or_create_from_event_data(data, network="canary")
        except Exception as e:
            logger.error("Error at canary_xx_sse_nodes_uptime_info_consumer: {}".format(str(e)))


@app.task(ignore_result=True)
def mainnet_xx_sse_nodes_uptime_info_consumer(**kwargs):
    while True:
        try:
            client = XxSSEClient(settings.XX_SSE_URLS["MAINNET"])
            for event in client.events():
                if event.event == "node_statuses_updated":
                    data = json.loads(event.data)
                    NodeInfo.objects.update_or_create_from_event_data(data, network="mainnet")
        except Exception as e:
            logger.error("Error at mainnet_xx_sse_nodes_uptime_info_consumer: {}".format(str(e)))


@app.task(ignore_result=True)
def users_node_uptime_notifier(**kwargs):
    node_info_pk = kwargs["node_info_pk"]
    node_status = kwargs["node_status"]
    node_network = kwargs["node_network"]

    node = NodeInfo.objects.get(pk=node_info_pk, network=node_network)

    for user in node.subscribed_users.all():
        bot.send_message(
            text=escape_markdown(
                get_node_status_info_text(
                    node_status,
                    node.node_id
                ),
                version=2
            ),
            chat_id=user.user_id,
            parse_mode=telegram.ParseMode.MARKDOWN_V2
        )
