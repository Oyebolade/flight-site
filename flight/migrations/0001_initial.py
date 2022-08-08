# Generated by Django 4.0.6 on 2022-07-27 20:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('country', models.CharField(max_length=70)),
                ('airport_code', models.CharField(max_length=3)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aeroplane', models.CharField(max_length=28)),
                ('departure_datetime', models.DateField(default=django.utils.timezone.now)),
                ('arrival_datetime', models.DateField(default=django.utils.timezone.now)),
                ('max_passenger', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('departure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin', to='flight.airport')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='flight.airport')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_no', models.CharField(max_length=6, unique=True)),
                ('passenger_first_name', models.CharField(blank=True, max_length=70)),
                ('passenger_last_name', models.CharField(blank=True, max_length=70)),
                ('booking_datetime', models.DateTimeField()),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.flight')),
            ],
        ),
    ]
