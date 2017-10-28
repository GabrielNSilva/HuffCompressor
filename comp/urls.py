from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^processed/$', views.processed, name='processed'),
    url(r'^cong/$', views.congratz, name='congratz'),
]
