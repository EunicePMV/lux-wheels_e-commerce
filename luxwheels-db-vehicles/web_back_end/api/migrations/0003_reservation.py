# Generated by Django 4.0.5 on 2022-07-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_user_firstname_remove_user_lastname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=27)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.BigIntegerField()),
                ('payment_method', models.TextField()),
                ('insurance_plan', models.TextField()),
                ('warranty', models.TextField()),
                ('service_maintenance', models.TextField()),
                ('comment', models.TextField(blank=True)),
                ('received_email', models.BooleanField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
