# Generated by Django 3.2.5 on 2021-07-05 09:13

from django.db import migrations, models
import righteous.utils


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210705_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.ImageField(default=1, max_length=255, upload_to=righteous.utils.rename_imagefile_to_uuid),
            preserve_default=False,
        ),
    ]
