# Generated by Django 4.0.4 on 2022-05-05 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bathroom', models.IntegerField()),
                ('bedroom', models.IntegerField()),
                ('garden', models.IntegerField()),
                ('garage', models.IntegerField()),
                ('parking', models.IntegerField()),
                ('pet', models.BooleanField()),
                ('pool', models.BooleanField()),
            ],
        ),
    ]
