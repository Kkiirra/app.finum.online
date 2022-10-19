# Generated by Django 4.0 on 2022-10-17 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0016_delete_invoice_status_alter_invoice_invoice_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Sent', 'Sent'), ('Paid', 'Paid'), ('Canceled', 'Canceled')], max_length=255),
        ),
    ]
