# Generated by Django reports.1.7 on 2020-05-31 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0003_taskinterface'),
    ]

    operations = [
        migrations.CreateModel(
            name='RunTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField(default=0, verbose_name='任务id')),
            ],
        ),
    ]
