# Generated by Django 2.2.1 on 2019-06-14 07:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_edit'),
    ]

    operations = [
        migrations.AddField(
            model_name='edit',
            name='value',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
