# Generated by Django 2.2.28 on 2023-09-16 18:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0013_auto_20230916_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Дата платежа', models.DateTimeField(default=datetime.datetime.now)),
                ('rate', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Имя_тарифа', to='guide.Rate')),
            ],
        ),
        migrations.RenameModel(
            old_name='Messages',
            new_name='Message',
        ),
        migrations.RemoveField(
            model_name='usercustommodel',
            name='Дата платежа',
        ),
        migrations.AlterField(
            model_name='usercustommodel',
            name='Реферальный код',
            field=models.CharField(default='wypnudwi', max_length=8, unique=True),
        ),
        migrations.DeleteModel(
            name='Pays',
        ),
        migrations.AddField(
            model_name='pay',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]