# Generated by Django 5.0.2 on 2024-02-26 08:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storebackend', '0002_confirmemailtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmemailtoken',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation time'),
        ),
        migrations.AlterField(
            model_name='confirmemailtoken',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confirm_email_tokens', to=settings.AUTH_USER_MODEL, verbose_name="User's email confirmation token"),
        ),
    ]
