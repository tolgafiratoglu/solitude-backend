# Generated by Django 4.1.3 on 2022-11-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solitude', '0002_remove_server_deleted_remove_server_host_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='host',
            field=models.CharField(default='', max_length=255),
        ),
    ]