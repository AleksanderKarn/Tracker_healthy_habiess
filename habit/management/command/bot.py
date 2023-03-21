from django.core.management.base import BaseCommand
from telebot import TeleBot

from tracker_healthy_habies.settings import TG_TOKEN

token = TG_TOKEN

# Объявление переменной бота
bot = TeleBot(token, threaded=False)


# Название класса обязательно - "Command"
class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)  # Сохранение обработчиков
        bot.load_next_step_handlers()  # Загрузка обработчиков
        bot.infinity_polling()
