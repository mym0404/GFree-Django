# Generated by Django 2.2.1 on 2019-07-26 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20190617_0141'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassTemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField(choices=[(1, 'First'), (2, 'Second')])),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=20)),
                ('professor', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('size', models.IntegerField()),
                ('grade', models.IntegerField(choices=[(0, 'Zero'), (1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four')])),
                ('start1', models.TimeField(blank=True, null=True)),
                ('end1', models.TimeField(blank=True, null=True)),
                ('week1', models.CharField(blank=True, choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], max_length=20, null=True)),
                ('start2', models.TimeField(blank=True, null=True)),
                ('end2', models.TimeField(blank=True, null=True)),
                ('week2', models.CharField(blank=True, choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], max_length=20, null=True)),
                ('start3', models.TimeField(blank=True, null=True)),
                ('end3', models.TimeField(blank=True, null=True)),
                ('week3', models.CharField(blank=True, choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], max_length=20, null=True)),
                ('start4', models.TimeField(blank=True, null=True)),
                ('end4', models.TimeField(blank=True, null=True)),
                ('week4', models.CharField(blank=True, choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], max_length=20, null=True)),
                ('start5', models.TimeField(blank=True, null=True)),
                ('end5', models.TimeField(blank=True, null=True)),
                ('week5', models.CharField(blank=True, choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], max_length=20, null=True)),
            ],
        ),
    ]
