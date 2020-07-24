# Generated by Django 3.0.8 on 2020-07-23 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clubs', '0002_auto_20200723_0848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clubuserstatus',
            old_name='club_id',
            new_name='club',
        ),
        migrations.RenameField(
            model_name='clubuserstatus',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='clubuserstatus',
            name='status',
            field=models.IntegerField(choices=[(0, 'REQUEST'), (1, 'MEMBER')], default=0),
        ),
    ]
