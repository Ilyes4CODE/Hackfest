# Generated by Django 4.2.6 on 2024-04-16 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0004_ticket_event_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='Event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.event'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.student'),
        ),
    ]
