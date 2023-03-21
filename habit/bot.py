from notifiers import get_notifier

from tracker_healthy_habies.settings import TG_TOKEN

bot = get_notifier('telegram')

def notification(chat_id, message):
    if chat_id and message:
        bot.notify(token=TG_TOKEN, chat_id=chat_id, message=message)


