import sseclient
import requests
from django.conf import settings


def get_sse_client():
    headers = {'Accept': 'text/event-stream'}
    response = requests.get(settings.XX_SSE_URL, stream=True, headers=headers)
    client = sseclient.SSEClient(response)
    return client
