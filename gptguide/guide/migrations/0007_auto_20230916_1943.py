# Generated by Django 2.2.28 on 2023-09-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0006_auto_20230916_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercustommodel',
            name='Реферальный код',
            field=models.CharField(default='jgdemfij', max_length=8, unique=True),
        ),
    ]
