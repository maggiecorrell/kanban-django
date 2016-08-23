from django.conf.urls import url, include
from rest_framework import routers
from not_trello import views
from django.contrib import admin

# router = routers.DefaultRoute()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('not_trello.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^', include(router.urls)),
]
