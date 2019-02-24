from django.urls import include, path, re_path

from .views import ProductDetail


urlpatterns = [
    re_path(r'^(?P<slug>[-\w]+)/$', ProductDetail.as_view(), name='detail'),
]