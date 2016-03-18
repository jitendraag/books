# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'date created', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'date updated', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('pages', models.IntegerField()),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('rating', models.FloatField()),
                ('pubdate', models.DateField()),
                ('abstract', models.TextField()),
                ('category', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'date created', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'date updated', null=True)),
                ('authors', models.ManyToManyField(to='sawaal.Author')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('num_awards', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'date created', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'date updated', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(to='sawaal.Publisher'),
            preserve_default=True,
        ),
    ]
