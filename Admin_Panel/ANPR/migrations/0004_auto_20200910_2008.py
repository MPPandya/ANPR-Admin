# Generated by Django 3.1.1 on 2020-09-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ANPR', '0003_auto_20200910_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_no',
            field=models.BigIntegerField(max_length=10),
        ),
    ]
