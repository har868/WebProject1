# Generated by Django 2.0.3 on 2018-04-28 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LeaderBoard', '0005_auto_20180428_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='ranking',
        ),
        migrations.RemoveField(
            model_name='person',
            name='total',
        ),
    ]