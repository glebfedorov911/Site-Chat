# Generated by Django 2.2.28 on 2023-09-16 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0033_auto_20230917_0030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pay',
            old_name='date',
            new_name='date_of_pay',
        ),
        migrations.AlterField(
            model_name='usercustommodel',
            name='ref_code',
            field=models.CharField(default='wmdnbfca', max_length=8),
        ),
    ]