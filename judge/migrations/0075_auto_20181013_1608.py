# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-13 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0074_totp'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='time_bonus',
            field=models.IntegerField(default=0, help_text='Number of minutes to award an extra point for submitting before the contest end. Leave as 0 for no time bonus.', verbose_name='time bonus'),
        ),
        migrations.AddField(
            model_name='contestsubmission',
            name='bonus',
            field=models.IntegerField(default=0, verbose_name='bonus'),
        ),
        migrations.AddField(
            model_name='contest',
            name='first_submission_bonus',
            field=models.IntegerField(default=0, help_text='Bonus points for fully solving on first submission.', verbose_name='first try bonus'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='display_rank',
            field=models.CharField(choices=[(b'user', b'Normal User'), (b'setter', b'Problem Setter'), (b'exec', b'Exec'), (b'teacher', b'Teacher'), (b'admin', b'Admin')], default=b'user', max_length=10, verbose_name='display rank'),
        ),
    ]
