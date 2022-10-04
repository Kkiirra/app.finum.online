# Generated by Django 4.0 on 2022-10-04 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0006_alter_user_account_default_currency_and_more'),
        ('orders', '0010_alter_order_status_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='order',
            unique_together={('order_name', 'user_account')},
        ),
    ]
