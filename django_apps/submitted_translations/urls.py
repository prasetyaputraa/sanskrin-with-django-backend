from django.urls import path
from .views import DownloadDoc

urlpatterns = [
    path('download-doc/', DownloadDoc.as_view())
]