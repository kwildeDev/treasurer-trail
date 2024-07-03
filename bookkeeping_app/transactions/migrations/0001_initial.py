# Generated by Django 5.0.6 on 2024-07-03 12:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('account_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('account_type', models.CharField(max_length=50)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('party_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('party_name', models.CharField(max_length=255)),
                ('party_type', models.CharField(max_length=50)),
                ('contact_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('transaction_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.party')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JournalEntries',
            fields=[
                ('journal_entry_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('entry_date', models.DateField()),
                ('debit_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('credit_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.account')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.transaction')),
            ],
        ),
    ]
