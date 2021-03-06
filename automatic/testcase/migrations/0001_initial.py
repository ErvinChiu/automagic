# Generated by Django 3.0.2 on 2020-01-15 10:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('element', '0001_initial'),
        ('management', '0001_initial'),
        ('keywords', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testrailcaseid', models.CharField(blank=True, max_length=12, null=True)),
                ('casedesc', models.CharField(max_length=255, verbose_name='Title')),
                ('isenabled', models.BooleanField(default=True)),
                ('issmoke', models.BooleanField(default=False)),
                ('dependent', models.CharField(blank=True, max_length=8, null=True)),
                ('debuginfo', models.CharField(blank=True, max_length=9999, null=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now_add=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
                ('moduleid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.Module')),
                ('projectid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Caseset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descr', models.CharField(max_length=200)),
                ('caseid', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('isenabled', models.BooleanField(default=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stepid', models.IntegerField(blank=True, null=True)),
                ('descr', models.CharField(blank=True, max_length=200, null=True)),
                ('inputtext', models.CharField(blank=True, max_length=200, null=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
                ('caseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testcase.Case')),
                ('elementid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='element.Element')),
                ('keywordid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='keywords.Keyword')),
            ],
        ),
    ]
