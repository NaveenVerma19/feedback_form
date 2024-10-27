# Generated by Django 5.1.2 on 2024-10-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TourFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('tour_start_date', models.DateField(null=True)),
                ('vehicle_condition', models.IntegerField()),
                ('driver_support', models.IntegerField()),
                ('guide_support', models.IntegerField()),
                ('hotels_chosen', models.IntegerField()),
                ('ground_support_team', models.IntegerField()),
                ('destination_rating', models.IntegerField()),
                ('tour_services_rating', models.IntegerField()),
                ('improve_services', models.TextField()),
            ],
        ),
    ]
