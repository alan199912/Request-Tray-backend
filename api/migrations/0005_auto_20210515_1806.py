# Generated by Django 3.2.3 on 2021-05-15 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210515_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='applycredituser',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='applycredituser',
            name='defaulter',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='applycredituser',
            name='indicator',
            field=models.IntegerField(default=5),
        ),
    ]
