from django.urls import path, include
from . import views

urlpatterns=[
    path('broadcast', views.broadcast_sms, name="default"),
    path('incoming', views.incoming_sms, name="incoming"),
]