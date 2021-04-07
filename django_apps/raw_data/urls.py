from django.urls import path
from .views import DownloadInUse

urlpatterns = [
    path('download-in-use/', DownloadInUse.as_view())
]