# Generated by Django 2.0.5 on 2018-05-16 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20180515_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(default=9800424333, max_length=10),
            preserve_default=False,
        ),
    ]