from notifiers import get_notifier

from tracker_healthy_habies.settings import TG_TOKEN, CHAT_ID

token = TG_TOKEN
chat_id = CHAT_ID


def funk(what):

    telegram = get_notifier("telegram")
    telegram.notify(token=token, chat_id=chat_id, message=what)



