# Generated by Django 2.2.28 on 2023-09-16 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0015_auto_20230916_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercustommodel',
            name='Реферальный код',
            field=models.CharField(default='hxheaqbk', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='usercustommodel',
            name='Слаг',
            field=models.SlugField(default=models.CharField(max_length=255, unique=True), unique=True),
        ),
    ]