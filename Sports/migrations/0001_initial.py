# Generated by Django 3.0.8 on 2020-07-20 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0)),
            ],
        ),
    ]
