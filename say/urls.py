from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.ask, name='ask'),
	url(r'^ans/$', views.ans, name='ans')
    ]
