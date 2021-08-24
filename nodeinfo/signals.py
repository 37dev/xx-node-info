from django.db.models.signals import pre_save
from django.dispatch import receiver

from nodeinfo.models import NodeInfo
from nodeinfo.tasks import users_node_uptime_notifier


@receiver(pre_save, sender=NodeInfo)
def uptime_notification_trigger(sender, instance, **kwargs):
    if instance.pk:
        old_instance = sender.objects.get(pk=instance.pk)
        if old_instance.status != instance.status and instance.has_subscribers:
            notifier_info = {
                "node_info_pk": instance.pk,
                "node_status": instance.status
            }
            users_node_uptime_notifier.apply_async(kwargs=notifier_info)
