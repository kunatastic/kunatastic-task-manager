# Generated by Django 3.2.12 on 2022-02-11 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20220210_1102'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TaskHistory',
        ),
    ]