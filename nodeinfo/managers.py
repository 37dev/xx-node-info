from django.db import models


class NodeInfoManager(models.Manager):
    def update_or_create_from_event_data(self, event_data):
        for node_id, status in event_data.items():
            node_info, _ = self.update_or_create(
                node_id=node_id, defaults={
                    "status": status.capitalize()
                }
            )
