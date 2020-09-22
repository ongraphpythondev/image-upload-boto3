from django.urls import path, include
from rest_framework.routers import DefaultRouter
from upload.views import ImageUploadViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'image-upload', ImageUploadViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
