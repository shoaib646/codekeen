from django.urls import path, include
from . import views



urlpatterns = [
    path(r"",views.HomePage, name='HomePage')
]