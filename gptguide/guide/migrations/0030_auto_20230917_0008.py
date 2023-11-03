# Generated by Django 2.2.28 on 2023-09-16 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0029_auto_20230917_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='Количество сообщений',
            field=models.CharField(blank=True, choices=[('M1', 10), ('M2', 15), ('M3', 20)], max_length=2),
        ),
        migrations.AlterField(
            model_name='rate',
            name='Цена',
            field=models.CharField(choices=[('C1', 100), ('C2', 200), ('C3', 300)], max_length=2),
        ),
        migrations.AlterField(
            model_name='usercustommodel',
            name='ref_code',
            field=models.CharField(default='capfxatv', max_length=8),
        ),
    ]