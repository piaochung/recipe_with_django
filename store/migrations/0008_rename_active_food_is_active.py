# Generated by Django 3.2.5 on 2021-07-05 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_food_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='active',
            new_name='is_active',
        ),
    ]
