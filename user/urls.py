from django.conf.urls import url
from user import views

urlpatterns = [
	url(r'^(?P<user_id>[0-9]+)/$', views.edition, name="edition")
]