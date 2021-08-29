from django.db import models, transaction


class NodeInfoManager(models.Manager):
    @transaction.atomic
    def update_or_create_from_event_data(self, event_data, network):
        for node_id, status in event_data.items():
            node_info, _ = self.update_or_create(
                node_id=node_id,
                network=network,
                defaults={
                    "status": status
                }
            )
