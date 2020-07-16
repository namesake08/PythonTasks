from django.conf.urls import url

from randomname import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^member_api$', views.members, name='member_api'),
]
