# Generated by Django 2.0.3 on 2018-04-28 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LeaderBoard', '0004_auto_20180427_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='User_id',
            new_name='ScreenName',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='Username',
        ),
    ]