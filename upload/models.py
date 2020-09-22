from django.db import models
from utils.s3_storage_services import PrivateMediaStorage


class ImageUpload(models.Model):
    public_image = models.ImageField(upload_to='PublicImage')
    private_image = models.FileField(upload_to='PrivateImage', storage=PrivateMediaStorage())

    class Meta:
        verbose_name_plural = 'Image Upload'
