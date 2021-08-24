from nodeinfo.models import NodeInfo
from tgbot.handlers import static_text
from tgbot.models import User
from tgbot.utils import reply


def command_start(update, context):
    u, created = User.get_user_and_created(update, context)

    if created:
        text = static_text.start_text.format(first_name=u.first_name)
    else:
        text = static_text.already_started_text

    reply(update, text)


def command_subscribe(update, context):
    node = NodeInfo.get_node_from_context(context)
    user = User.get_user(update, context)

    if not node:
        reply(update, static_text.node_id_does_not_exist_text)
        return

    is_user_subscribed = node.is_user_subscribed(user)

    if not is_user_subscribed:
        node.subscribed_users.add(user)
        reply(update, static_text.node_subscribe_text.format(node.status))
    else:
        reply(update, static_text.node_already_subscribed_text)


def command_unsubscribe(update, context):
    node = NodeInfo.get_node_from_context(context)
    user = User.get_user(update, context)

    if not node:
        reply(update, static_text.node_id_does_not_exist_text)
        return

    is_user_subscribed = node.is_user_subscribed(user)

    if is_user_subscribed:
        node.subscribed_users.remove(user)
        reply(update, static_text.node_unsubscribe_text)
    else:
        reply(update, static_text.node_already_unsubscribed_text)
