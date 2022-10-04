# Generated by Django 4.0 on 2022-10-04 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0006_alter_user_account_default_currency_and_more'),
        ('company', '0004_alter_company_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='company',
            unique_together={('company_name', 'user_account')},
        ),
    ]
