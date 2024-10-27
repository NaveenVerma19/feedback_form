# Generated by Django 5.1.2 on 2024-10-27 09:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='tourfeedback',
            name='destination_rating',
        ),
        migrations.RemoveField(
            model_name='tourfeedback',
            name='driver_support',
        ),
        migrations.RemoveField(
            model_name='tourfeedback',
            name='ground_support_team',
        ),
        migrations.RemoveField(
            model_name='tourfeedback',
            name='guide_support',
        ),
        migrations.RemoveField(
            model_name='tourfeedback',
            name='hotels_chosen',
        ),
        migrations.RemoveField(
            model_name='tourfeedback',
            name='improve_services',
        ),
        migrations.RemoveField(
            model_name='tourfeedback',
            name='tour_services_rating',
        ),
        migrations.AlterField(
            model_name='tourfeedback',
            name='vehicle_condition',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='ReviewRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=100)),
                ('review', models.TextField(blank=True, max_length=500)),
                ('rating', models.FloatField()),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedbacks.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedbacks.account')),
            ],
        ),
    ]