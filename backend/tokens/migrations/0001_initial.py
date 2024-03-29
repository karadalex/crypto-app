# Generated by Django 3.1.4 on 2020-12-26 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoCurrency',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('symbol', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FiatCurrency',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('symbol', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PriceRecord',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('from_id', models.PositiveIntegerField()),
                ('from_amount', models.FloatField()),
                ('to_id', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('from_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_price_records', to='contenttypes.contenttype')),
                ('to_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_price_records', to='contenttypes.contenttype')),
            ],
        ),
    ]
