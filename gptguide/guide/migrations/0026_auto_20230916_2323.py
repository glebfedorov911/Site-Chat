# Generated by Django 2.2.28 on 2023-09-16 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0025_auto_20230916_2318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercustommodel',
            old_name='Количество доступных сообщений',
            new_name='msg',
        ),
        migrations.AlterField(
            model_name='usercustommodel',
            name='ref_code',
            field=models.CharField(default='oiprtrpt', max_length=8),
        ),
    ]
