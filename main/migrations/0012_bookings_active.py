# Generated by Django 5.0.2 on 2024-02-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_bookings_entry_date_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='active',
            field=models.CharField(default='', max_length=10),
        ),
    ]
