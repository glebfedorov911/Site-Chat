# Generated by Django 2.2.28 on 2023-09-16 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0030_auto_20230917_0008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='Цена',
            new_name='cost',
        ),
        migrations.RenameField(
            model_name='rate',
            old_name='Количество сообщений',
            new_name='count_message',
        ),
        migrations.RenameField(
            model_name='rate',
            old_name='Название тарифа',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='usercustommodel',
            name='ref_code',
            field=models.CharField(default='kdoduipl', max_length=8),
        ),
    ]
