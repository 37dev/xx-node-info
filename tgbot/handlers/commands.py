from tgbot.handlers.utils import handler_logging
from tgbot.models import User


@handler_logging()
def command_start(update, context):
    u, created = User.get_user_and_created(update, context)

    if created:
        text = "Welcome {first_name}".format(first_name=u.first_name)
    else:
        text = "You have started the bot already"

    update.message.reply_text(text=text)
