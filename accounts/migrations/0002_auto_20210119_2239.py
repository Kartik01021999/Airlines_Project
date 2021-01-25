# Generated by Django 2.2.17 on 2021-01-20 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='End',
            field=models.CharField(default='10:00', max_length=10),
        ),
        migrations.AddField(
            model_name='flights',
            name='Price',
            field=models.IntegerField(default=2000),
        ),
        migrations.AddField(
            model_name='flights',
            name='Start',
            field=models.CharField(default='10:00', max_length=10),
        ),
    ]