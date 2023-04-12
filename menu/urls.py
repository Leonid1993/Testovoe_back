
from django.urls import path

from .views import BaseView

urlpatterns = [
    path('<str:slug>', BaseView.as_view(), name='menu'),
]