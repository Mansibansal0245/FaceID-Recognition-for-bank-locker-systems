# Generated by Django 2.0 on 2018-01-04 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log_in', '0012_merge_20180104_0708'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='myuser',
            unique_together={('email',)},
        ),
    ]