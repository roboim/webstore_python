from typing import Type

from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal

from storebackend.models import User

new_user_registered = Signal()


@receiver(post_save, sender=User)
def new_user_created_signal(sender: Type[User], instance: User, created: bool, **kwargs):
    """
    Отправка письма для подтверждения регистрации
    """
    if created and not instance.is_active:
        message_body = (
            f"Добрый день, {instance.first_name}! Если Вы не регистрировались в магазине, пожалуйста, "
            f"сообщите администратору. "
            f"Для авторизации воспользуйтесь url: webstore_python/token/ для получения access и refresh токенов.")
        send_mail('Вы зарегистрировались в webstore_python', message_body,
                  settings.EMAIL_HOST_USER, [instance.email])
