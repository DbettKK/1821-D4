# Generated by Django 3.1 on 2020-08-11 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20200811_1527'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-create_time']},
        ),
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ['-create_time']},
        ),
        migrations.AlterModelOptions(
            name='modify',
            options={'ordering': ['-time']},
        ),
        migrations.AlterModelOptions(
            name='teammember',
            options={'ordering': ['-join_time']},
        ),
        migrations.AlterModelOptions(
            name='userbrowsefile',
            options={'ordering': ['-last_modified']},
        ),
        migrations.AlterModelOptions(
            name='userkeptfile',
            options={'ordering': ['-kept_time']},
        ),
    ]
