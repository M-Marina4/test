# Generated by Django 4.2.4 on 2023-08-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_homepage_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='paragraph_1',
            field=models.TextField(),
        ),
    ]