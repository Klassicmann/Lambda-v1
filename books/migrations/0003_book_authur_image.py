# Generated by Django 2.2 on 2020-01-06 10:34

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200106_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authur_image',
            field=imagekit.models.fields.ProcessedImageField(default='default.png', upload_to='books/authur_images'),
        ),
    ]
