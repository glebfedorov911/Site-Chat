# Generated by Django 2.2.28 on 2023-09-16 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0031_auto_20230917_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='cost',
            field=models.CharField(choices=[('100', 100), ('200', 200), ('300', 300)], max_length=50),
        ),
        migrations.AlterField(
            model_name='rate',
            name='count_message',
            field=models.CharField(blank=True, choices=[('10', 10), ('20', 15), ('30', 20)], max_length=50),
        ),
        migrations.AlterField(
            model_name='rate',
            name='name',
            field=models.CharField(choices=[('Минимальный', 'Минимальный'), ('Cредний', 'Cредний'), ('Максимальный', 'Максимальный')], max_length=50),
        ),
        migrations.AlterField(
            model_name='usercustommodel',
            name='ref_code',
            field=models.CharField(default='egyjsmlw', max_length=8),
        ),
    ]
