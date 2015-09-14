# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='title',
        ),
        migrations.AddField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 14, 3, 47, 10, 146495, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='done',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='owner',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 14, 3, 47, 29, 524354, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
