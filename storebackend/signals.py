from typing import Type

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal

from storebackend.models import User

new_user_registered = Signal()


@receiver(post_save, sender=User)
def new_user_created_signal(sender, instance, created, **kwargs):
    """
    Отправка письма для подтверждения почтового адреса
    """
    print('SIGNALS')
