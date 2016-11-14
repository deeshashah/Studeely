# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='favourite_hamster_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fblink',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gplink',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='shortbio',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twlink',
            field=models.URLField(null=True, blank=True),
        ),
    ]
