from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("mansoorauth/", admin.site.urls),
    path('', include('basepage.urls'))
]

