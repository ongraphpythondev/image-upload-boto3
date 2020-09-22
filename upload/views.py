from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from upload.models import ImageUpload
from upload.serializers import ImageUploadSerializer


class ImageUploadViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing image instances.
    """
    permission_classes = (IsAuthenticated,)

    serializer_class = ImageUploadSerializer
    queryset = ImageUpload.objects.all()
