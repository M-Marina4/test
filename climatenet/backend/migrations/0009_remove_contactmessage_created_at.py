# Generated by Django 4.2.4 on 2023-08-29 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_alter_contactmessage_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmessage',
            name='created_at',
        ),
    ]