# Generated by Django 4.0 on 2022-09-24 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0004_alter_bank_account_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank_account',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]