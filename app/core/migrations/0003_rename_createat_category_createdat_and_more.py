# Generated by Django 5.0.3 on 2024-04-26 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_category_tag_remove_task_createat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='createAt',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='updateAt',
            new_name='updatedAt',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='createAt',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='updateAt',
            new_name='updatedAt',
        ),
    ]
