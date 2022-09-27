# Generated by Django 4.0 on 2022-09-24 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0006_alter_user_account_default_currency_and_more'),
        ('integrations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank_account',
            name='user_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_account', to='customuser.user_account'),
        ),
    ]
