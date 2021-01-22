from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'df_coupon'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    #path('scene/',views.scene),
    url(r'^scene/$', views.scene,name="scene")
    #url(r'^scene$', views.scene, name="scene")
]
