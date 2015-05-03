# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blog_heading', models.CharField(max_length=200)),
                ('blog_subheading', models.CharField(max_length=200)),
                ('blog_pub_date', models.DateTimeField(verbose_name=b'date blog published')),
                ('blog_content', models.TextField(verbose_name=b'blog content')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
