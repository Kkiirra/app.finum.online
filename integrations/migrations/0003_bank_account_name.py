# Generated by Django 4.0 on 2022-09-24 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0002_alter_bank_account_user_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_account',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
