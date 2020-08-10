# Generated by Django 3.1 on 2020-08-10 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('president_name', models.CharField(default='Megha', max_length=150)),
                ('club_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('logo', models.ImageField(upload_to='')),
            ],
        ),
    ]
