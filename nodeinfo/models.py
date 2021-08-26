from django.db import models

from nodeinfo.managers import NodeInfoManager


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
    def get_node_from_context(cls, context):
        node_id = context.args[0]
        node = cls.objects.filter(node_id=node_id).first()

        return node

    @staticmethod
    def get_node_network():
        pass
