from __future__ import absolute_import
try:
    from django.conf.urls import re_path, include
except ImportError:
    from django.urls import re_path, include
from . import views

app_urlpatterns = [
    re_path(r'^1c_exchange.php$', views.front_view, name='front_view'),
    re_path(r'^exchange$', views.front_view, name='front_view'),
]

urlpatterns = [
    re_path(r'^', include((app_urlpatterns, 'cml'), namespace='cml')),
]
