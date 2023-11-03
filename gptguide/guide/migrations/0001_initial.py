# Generated by Django 2.2.28 on 2023-09-15 19:03

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCustomModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Логин', models.CharField(max_length=255, unique=True)),
                ('Регистрация', models.CharField(max_length=255)),
                ('Рефералка', models.BooleanField(default=False)),
                ('Количество доступных сообщений', models.IntegerField()),
                ('Реферальный код', models.CharField(max_length=8)),
                ('Скидка', models.IntegerField()),
                ('Слаг', models.SlugField(unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Название тарифа', models.CharField(choices=[('R1', 'Тариф1'), ('R2', 'Тариф2'), ('R3', 'Тариф3')], max_length=2)),
                ('Цена', models.IntegerField(choices=[('C1', 'Цена1'), ('C2', 'Цена2'), ('C3', 'Цена3')])),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Текст сообщения', models.TextField()),
                ('from_user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='отправитель', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='получатель', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='usercustommodel',
            name='rate',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Юзер', to='guide.Rate'),
        ),
        migrations.AddField(
            model_name='usercustommodel',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
