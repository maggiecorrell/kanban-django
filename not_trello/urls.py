from django.conf.urls import url
from . import views
from .views import BoardViewSet
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^login/index/$', views.index, name='index'),
    url(r'^register/$', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreationForm,
            success_url='/'

    ), name='register'),
    url(r'^$', login, name='login'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/login'}, name='logout'),
    url(r'^board/(?P<pk>[0-9]+)', views.board, name='board')
    ]

# url(r'^/users/', ListCreateAPIView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='user-list')
# ]
