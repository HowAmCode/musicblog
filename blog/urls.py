from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^toronto/', views.post_list_toronto, name='post_list_toronto'),
	url(r'^about/', views.about_us, name='about_us'),
]