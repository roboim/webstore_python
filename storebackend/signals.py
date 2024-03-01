from typing import Type

from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal

from storebackend.models import User, ConfirmEmailToken

new_user_registered = Signal()
new_order = Signal()


@receiver(post_save, sender=User)
def new_user_created_signal(sender: Type[User], instance: User, created: bool, **kwargs):
    """
    Отправка письма для подтверждения регистрации
    """
    if created and not instance.is_active:
        token, _ = ConfirmEmailToken.objects.get_or_create(user_id=instance.pk)
        message_body = (
            f"Добрый день, {instance.first_name}! Если Вы не регистрировались в магазине, пожалуйста, "
            f"сообщите администратору. /n"
            f"Для авторизации воспользуйтесь url: webstore_python/user/create/confirm и укажите "
            f"токен: {token.key}")
        send_mail('Вы зарегистрировались в webstore_python', message_body,
                  settings.EMAIL_HOST_USER, [instance.email])
        # print(message_body)


@receiver(new_order)
def new_order_created_signal(user_email, user_first_name, **kwargs):
    """
    Отправка письма для создания заказа
    """
    message_body = (
        f"Добрый день, {user_first_name}! От Вашего лица поступил запрос на новый заказ."
        f"Ожидайте, пожалуйста, подтверждения от консультанта магазина.")
    send_mail('Подтверждение получения нового заказа', message_body,
              settings.EMAIL_HOST_USER, [user_email])
