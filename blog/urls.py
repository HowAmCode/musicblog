from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^toronto/', views.post_list_toronto, name='post_list_toronto'),
	url(r'^about/', views.about_us, name='about_us'),
]