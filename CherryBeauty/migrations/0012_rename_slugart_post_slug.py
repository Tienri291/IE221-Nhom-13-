# Generated by Django 3.2.9 on 2022-05-10 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CherryBeauty', '0011_rename_slug_post_slugart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slugart',
            new_name='slug',
        ),
    ]
