from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^appreq$', views.appreq, name='appreq'),
    url(r'^registration$', views.users, name='users'),
    url(r'^redirect$', views.redirect, name='redirect'),
    url(r'^login$',views.home,name='home'),
    url(r'^$',views.pagemain,name='pagemain'),
    url(r'^list$',views.list,name='list'),
]
