# Generated by Django 3.1.4 on 2020-12-29 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201229_1235'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Status',
        ),
    ]
