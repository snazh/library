from django.contrib import admin
from django.urls import path
from main.views import BookAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/booklist/', BookAPIView.as_view())
]
