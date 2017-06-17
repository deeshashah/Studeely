# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20151001_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='shortbio',
            field=models.TextField(max_length=100, null=True, blank=True),
        ),
    ]
