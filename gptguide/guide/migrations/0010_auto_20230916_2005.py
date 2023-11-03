# Generated by Django 2.2.28 on 2023-09-16 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0009_auto_20230916_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercustommodel',
            name='rate',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Тариф', to='guide.Rate'),
        ),
        migrations.AlterField(
            model_name='usercustommodel',
            name='Реферальный код',
            field=models.CharField(default='hdtvrxrg', max_length=8, unique=True),
        ),
    ]