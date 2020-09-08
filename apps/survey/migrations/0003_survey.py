# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20160226_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age_range', models.IntegerField(default=0, null=True, blank=True)),
                ('languages', jsonfield.fields.JSONField(null=True, verbose_name=b'What languages do you speak other than English?', blank=True)),
                ('familiarity_w_technology', models.IntegerField(default=0, verbose_name=b'How familiar are you with working with computer technology on a scale of 1 to 10? 1 being "not familiar at all" and 10 being "extremely familiar."')),
            ],
        ),
    ]
