# Generated by Django 4.2.4 on 2023-08-15 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_homepage_paragraph_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='phone',
            field=models.CharField(default=123, max_length=50),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('device_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.devicedetails')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.region')),
            ],
        ),
    ]
