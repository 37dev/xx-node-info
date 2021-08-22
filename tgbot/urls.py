from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from . import views

urlpatterns = [  
    path(settings.WEBHOOK_SECRET_ENDPOINT, csrf_exempt(views.TelegramBotWebhookView.as_view())),
]
