# Generated by Django 2.2.28 on 2023-10-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0048_auto_20231019_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='audio/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='usercustommodel',
            name='ref_code',
            field=models.CharField(default='bvintggq', max_length=8),
        ),
    ]
