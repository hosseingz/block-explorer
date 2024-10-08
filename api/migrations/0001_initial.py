# Generated by Django 5.0 on 2024-09-19 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_id', models.PositiveIntegerField()),
                ('timestamp', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_address', models.CharField(max_length=128, verbose_name='from')),
                ('to_address', models.CharField(max_length=128)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=30)),
                ('txID', models.CharField(max_length=64)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='api.block')),
            ],
        ),
    ]
