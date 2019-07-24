# Generated by Django 2.2.1 on 2019-06-14 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20190521_0118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField(choices=[(1, 'First'), (2, 'Second')])),
                ('writer', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('ADD', 'ADD'), ('REMOVE', 'REMOVE'), ('CODE', 'CODE'), ('NAME', 'NAME'), ('GRADE', 'GRADE'), ('PROFESSOR', 'PROFESSOR'), ('PLACE', 'PLACE'), ('SIZE', 'SIZE'), ('TIMEADD', 'TIMEADD'), ('TIMEREMOVE', 'TIMEREMOVE'), ('TIME', 'TIME')], max_length=20)),
                ('editClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Class')),
            ],
        ),
    ]
