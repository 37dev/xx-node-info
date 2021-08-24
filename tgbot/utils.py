import telegram
from telegram.utils.helpers import escape_markdown

from tgbot.handlers import static_text


def extract_user_data_from_update(update):
    """ python-telegram-bot's Update instance --> User info """
    if update.message is not None:
        user = update.message.from_user.to_dict()
    elif update.inline_query is not None:
        user = update.inline_query.from_user.to_dict()
    elif update.chosen_inline_result is not None:
        user = update.chosen_inline_result.from_user.to_dict()
    elif update.callback_query is not None and update.callback_query.from_user is not None:
        user = update.callback_query.from_user.to_dict()
    elif update.callback_query is not None and update.callback_query.message is not None:
        user = update.callback_query.message.chat.to_dict()
    else:
        raise Exception(f"Can't extract user data from update: {update}")

    return dict(
        user_id=user["id"],
        is_blocked_bot=False,
        **{
            k: user[k]
            for k in ["username", "first_name", "last_name", "language_code"]
            if k in user and user[k] is not None
        },
    )


def reply(update, text):
    update.message.reply_text(
        text=escape_markdown(text, version=2),
        parse_mode=telegram.ParseMode.MARKDOWN_V2
    )


def get_node_status_info_text(status, node_id):
    if status == "Online":
        return static_text.node_status_text.format(emoji="✅", status=status, node_id=node_id)
    else:
        return static_text.node_status_text.format(emoji="🚨", status=status, node_id=node_id)
