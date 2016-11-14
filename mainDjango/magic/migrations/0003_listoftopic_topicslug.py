# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0002_auto_20151001_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='listoftopic',
            name='topicSlug',
            field=models.CharField(default=datetime.datetime(2015, 10, 9, 13, 14, 18, 975847, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
