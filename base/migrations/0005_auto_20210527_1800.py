# Generated by Django 3.2.2 on 2021-05-27 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20210527_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bug',
            old_name='b_attachment',
            new_name='attachment',
        ),
        migrations.RenameField(
            model_name='bug',
            old_name='b_image',
            new_name='image',
        ),
    ]
