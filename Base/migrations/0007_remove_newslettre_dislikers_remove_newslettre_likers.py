# Generated by Django 4.2.6 on 2024-04-16 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0006_remove_ticket_place_event_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newslettre',
            name='dislikers',
        ),
        migrations.RemoveField(
            model_name='newslettre',
            name='likers',
        ),
    ]
