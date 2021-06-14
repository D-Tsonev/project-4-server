# Generated by Django 3.2.4 on 2021-06-14 13:05

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=500)),
                ('profile_image', models.CharField(default='https://www.clipartkey.com/mpngs/m/152-1520367_user-profile-default-image-png-clipart-png-download.png', max_length=250)),
                ('user_type', models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher')], max_length=10)),
                ('instrument_type', models.CharField(choices=[('Piano', 'Piano'), ('Drums', 'Drums'), ('Timpani', 'Timpani'), ('Xylophone', 'Xylophone'), ('Cornet', 'Cornet'), ('Tuba', 'Tuba'), ('Trombone', 'Trombone'), ('French Horn', 'French Horn'), ('Trumpet', 'Trumpet'), ('Saxophone', 'Saxophone'), ('Bassoon', 'Bassoon'), ('Clarinet', 'Clarinet'), ('Oboe', 'Oboe'), ('Flute', 'Flute'), ('Guitar', 'Guitar'), ('Harp', 'Harp'), ('Double Bass', 'Double Bass'), ('Cello', 'Cello'), ('Viola', 'Viola'), ('Violin', 'Violin')], max_length=15)),
                ('location_type_choices', models.CharField(choices=[('London', 'London'), ('Manchester', 'Manchester'), ('Birmingham', 'Birmingham'), ('Liverpool', 'Liverpool'), ('Leeds', 'Leeds'), ('Newcastle', 'Newcastle'), ('Edinburgh', 'Edinburgh'), ('Glasgow', 'Glasgow'), ('Cambridge', 'Cambridge'), ('Bristol', 'Bristol'), ('Cardiff', 'Cardiff'), ('Belfast', 'Belfast'), ('York', 'York'), ('Sheffield', 'Sheffield')], max_length=15)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
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
    ]
