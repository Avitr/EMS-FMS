# Generated by Django 2.0.5 on 2018-05-15 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
