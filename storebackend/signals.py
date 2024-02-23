from typing import Type

from django.conf import settings
from django.core.mail import EmailMultiAlternatives, send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal

from storebackend.models import User

new_user_registered = Signal()


@receiver(post_save, sender=User)
def new_user_created_signal(sender: Type[User], instance: User, created: bool, **kwargs):
    """
    Отправка письма для подтверждения почтового адреса
    """
    print('SIGNALS')
    if created and not instance.is_active:
        message_body = "Тестовое сообщение от Django!"
        send_mail('Тема', message_body, settings.EMAIL_HOST_USER, ['test@yandex.ru'])