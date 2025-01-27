# Generated by Django 5.0.2 on 2024-02-25 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('ticket_id', models.CharField(max_length=50)),
                ('vehicle_no', models.CharField(max_length=50)),
                ('vehicle_type', models.CharField(max_length=50)),
                ('block_id', models.CharField(max_length=10)),
                ('slot_no', models.CharField(max_length=10)),
                ('entry_date_time', models.DateTimeField()),
                ('exit_date_time', models.DateTimeField()),
            ],
        ),
    ]
