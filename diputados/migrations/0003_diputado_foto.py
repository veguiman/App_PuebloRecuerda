# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diputados', '0002_auto_20161103_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='diputado',
            name='foto',
            field=models.ImageField(null=True, upload_to='/assets/images'),
        ),
    ]
