# Generated by Django 2.2.28 on 2023-09-16 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0026_auto_20230916_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercustommodel',
            name='ref_code',
            field=models.CharField(default='irpbhbaj', max_length=8),
        ),
    ]