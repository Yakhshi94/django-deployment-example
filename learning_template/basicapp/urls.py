from django.urls import re_path
from basicapp import views

# TEMPLATE TAGGING
app_name = 'basicapp'

urlpatterns = [
    re_path(r'^relative/$', views.relatives, name='relatives'),
    re_path(r'^other/$', views.other, name='other'),
]
