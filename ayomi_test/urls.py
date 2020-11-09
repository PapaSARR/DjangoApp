from django.conf.urls import url
from django.urls import include
from user import views


urlpatterns = [
    url(r'^$', views.connexion, name="connexion"),
    url(r'^user/', include('user.urls'))
]

