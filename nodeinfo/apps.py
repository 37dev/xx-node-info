from django.apps import AppConfig


class NodeinfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nodeinfo'

    def ready(self):
        from nodeinfo.signals import uptime_notification_trigger
