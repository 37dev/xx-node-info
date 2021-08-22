import json
import logging
from django.views import View
from django.http import JsonResponse

from tgbot.tasks import process_telegram_event

logger = logging.getLogger(__name__)


class TelegramBotWebhookView(View):
    def post(self, request, *args, **kwargs):
        process_telegram_event.delay(json.loads(request.body))
        return JsonResponse({"message": "ok"}, status=200)

    def get(self, request):
        return JsonResponse({"message": "ok"}, status=200)
