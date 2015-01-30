# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment_Stage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('visit_count', models.IntegerField(default=0)),
                ('completed_count', models.IntegerField(default=0)),
                ('prescribed_time', models.IntegerField(default=0)),
                ('max_score', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Experiments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('lab_category', models.CharField(max_length=200)),
                ('lang', models.CharField(max_length=200)),
                ('visit_count', models.IntegerField(default=0)),
                ('completed_count', models.IntegerField(default=0)),
                ('creation_date', models.DateTimeField(verbose_name=b'creation date')),
                ('last_mod_date', models.DateTimeField(verbose_name=b'last modified date')),
                ('prescribed_time', models.IntegerField(default=0)),
                ('max_score', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_Experiment_Stage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('attempt', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_Experiments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('mode', models.CharField(max_length=10, choices=[(b'free style', b'test mode')])),
                ('experiment', models.ForeignKey(to='NLP.Experiments')),
                ('max_stage', models.ForeignKey(to='NLP.Experiment_Stage')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('institute', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='user_experiment_stage',
            name='experiment',
            field=models.ForeignKey(to='NLP.User_Experiments'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_experiment_stage',
            name='experiment_stage',
            field=models.ForeignKey(to='NLP.Experiment_Stage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_experiment_stage',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experiment_stage',
            name='experiment',
            field=models.ForeignKey(to='NLP.Experiments'),
            preserve_default=True,
        ),
    ]
