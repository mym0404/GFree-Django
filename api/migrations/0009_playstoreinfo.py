# Generated by Django 2.2.1 on 2019-05-11 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190512_0536'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayStoreInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('versionName', models.CharField(max_length=50)),
                ('versionCode', models.IntegerField()),
            ],
        ),
    ]
