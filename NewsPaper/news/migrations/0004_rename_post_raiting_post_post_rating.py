# Generated by Django 4.2.5 on 2023-09-22 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_categories_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_raiting',
            new_name='post_rating',
        ),
    ]
