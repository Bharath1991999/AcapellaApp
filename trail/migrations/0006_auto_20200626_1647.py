# Generated by Django 3.0.7 on 2020-06-26 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trail', '0005_auto_20200625_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
