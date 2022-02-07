import sseclient
import requests
from django.conf import settings


class XxSSEClient(sseclient.SSEClient):
    def __init__(self, event_url):
        event_source = self._get_event_data(event_url)
        super().__init__(event_source)

    @staticmethod
    def _get_event_data(event_url):
        headers = {'Accept': 'text/event-stream'}
        response = requests.get(event_url, stream=True, headers=headers, timeout=settings.XX_SSE_TIMEOUT)
        return response

