# Generated by Django 5.0.6 on 2024-07-04 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='mail@mail.com', max_length=254),
            preserve_default=False,
        ),
    ]
