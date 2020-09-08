# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0034_state_subdivision_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurisdiction',
            name='city_label',
            field=models.CharField(default='City', max_length=250, verbose_name='Label for local government unit'),
        ),
    ]
