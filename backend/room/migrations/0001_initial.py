# Generated by Django 4.0.3 on 2022-03-16 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hostel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=5)),
                ('max_occupants', models.IntegerField()),
                ('room_available', models.BooleanField(default=True)),
                ('room_price', models.BigIntegerField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel.hostel')),
            ],
        ),
    ]
