from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'df_cart'

urlpatterns = [
    path('', views.add, name='add'),
    path('', views.modify, name='modify'),
    path('', views.show, name='show'),
    path('', views.delete, name='delete'),
    url(r'^push/$', views.push, name="push")
]