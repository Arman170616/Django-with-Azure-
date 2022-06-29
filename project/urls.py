
from django.contrib import admin
from django.urls import path, include

from relecloud import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('relecloud.urls')),
]
