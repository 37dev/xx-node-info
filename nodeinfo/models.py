from django.db import models

from nodeinfo.managers import NodeInfoManager
from tgbot.handlers import static_text
from tgbot.utils import reply


class NodeInfo(models.Model):
    name = models.CharField(max_length=200)
    node_id = models.CharField(max_length=200)
    group = models.CharField(max_length=200)
    application_id = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    round_failure_avg = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    status = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    uptime = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    application_url = models.CharField(max_length=200)
    subscribed_users = models.ManyToManyField('tgbot.User', related_name="subscribed_nodes")
    network = models.CharField(max_length=32, null=True)

    objects = NodeInfoManager()

    def __str__(self):
        return self.node_id

    @property
    def has_subscribers(self):
        has_subscribers = self.subscribed_users.exists()
        return has_subscribers

    def is_user_subscribed(self, user):
        user_already_subscribed = user.subscribed_nodes.filter(pk=self.pk).exists()
        return user_already_subscribed

    @classmethod
    def get_node_from_context(cls, update, context):
        try:
            node_id = context.args[0]
            network = context.args[1]
            node = cls.objects.get(node_id=node_id, network=network.lower())
            return node

        except IndexError:
            reply(update, static_text.invalid_subscription_format_text)
            return None

        except cls.DoesNotExist:
            reply(update, static_text.node_does_not_exist_text)
            return None

    @staticmethod
    def get_node_network():
        pass
