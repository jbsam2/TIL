# Generated by Django 3.1 on 2020-10-16 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20201016_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rank',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        ),
    ]
