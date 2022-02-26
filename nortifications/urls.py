from django.urls import path
from .views import *

urlpatterns = [
    path('notif', send_nortification),
]