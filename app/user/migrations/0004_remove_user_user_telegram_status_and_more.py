# Generated by Django 4.1 on 2023-11-06 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_user_telegram_status_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_telegram_status',
        ),
        migrations.AddField(
            model_name='user',
            name='telegram_password',
            field=models.CharField(default=None, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='telegram_password_expires',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
