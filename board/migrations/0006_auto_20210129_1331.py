# Generated by Django 2.0.13 on 2021-01-29 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_auto_20210127_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='context',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='result',
            field=models.FloatField(default=0),
        ),
    ]
