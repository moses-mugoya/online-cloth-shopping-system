# Generated by Django 2.0.6 on 2018-08-22 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_auto_20180822_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='credit_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='balance',
            name='security_code',
            field=models.IntegerField(null=True),
        ),
    ]
