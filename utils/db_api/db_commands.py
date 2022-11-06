from asgiref.sync import sync_to_async
from django.db import IntegrityError

from admin_panel.telebot.models import Clients


@sync_to_async()
def create_client(username, telegram_id, phone):
    Clients.objects.get_or_create(telegram_id=telegram_id, username=username, number=phone)


@sync_to_async()
def select_client(telegram_id):
    return Clients.objects.filter(telegram_id=telegram_id)


@sync_to_async()
def select_managers():
    return Clients.objects.all()
