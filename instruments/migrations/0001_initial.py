# Generated by Django 3.2.5 on 2021-07-02 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=5000)),
                ('instrument_family', models.CharField(choices=[('Strings', 'Strings'), ('Woodwind', 'Woodwind'), ('Brass', 'Brass'), ('Percussion', 'Percussion'), ('Keyboards', 'Keyboards')], max_length=50)),
                ('image', models.CharField(max_length=250)),
                ('media', models.CharField(max_length=250)),
            ],
        ),
    ]
