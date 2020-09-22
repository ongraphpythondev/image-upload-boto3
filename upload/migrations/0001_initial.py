# Generated by Django 3.1.1 on 2020-09-22 08:27

from django.db import migrations, models
import utils.s3_storage_services


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_image', models.ImageField(upload_to='PublicImage')),
                ('private_image', models.FileField(storage=utils.s3_storage_services.PrivateMediaStorage(), upload_to='PrivateImage')),
            ],
            options={
                'verbose_name_plural': 'Image Upload',
            },
        ),
    ]