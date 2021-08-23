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

    objects = NodeInfoManager()

    def __str__(self):
        return self.node_id
