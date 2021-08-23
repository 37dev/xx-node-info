import json

from celery.signals import worker_ready
from django.conf import settings

from clients.xx_sse_client import XxSSEClient
from dtb.celery import app
from nodeinfo.models import NodeInfo


@app.task(ignore_result=True, bind=True)
@worker_ready.connect
def xx_sse_nodes_uptime_info_consumer(sender, **kwargs):
    client = XxSSEClient(settings.XX_SSE_URL)

    for event in client.events():
        if event.event == "node_statuses_updated":
            data = json.loads(event.data)
            NodeInfo.objects.update_or_create_from_event_data(data)
