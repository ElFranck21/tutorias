# Generated by Django 5.0.6 on 2024-07-02 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0003_admin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Guest',
        ),
        migrations.DeleteModel(
            name='Principal',
        ),
    ]