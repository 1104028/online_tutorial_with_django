from django.conf.urls import url
from django.contrib.auth.views import login,logout,logout_then_login
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'onlinetut'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^courselist/$', views.HomepageView, name='homepage'),
    url(r'^register/$', views.registerUser, name='register'),
    url(r'^login/$', login, name='login'),
     url(r'^logout/$', logout, name='logout'),
     url(r'^logout-then-login/$', logout_then_login, name='logouthenlogin'),
     url(r'^course_detail/(?P<pk>[0-9]+)/$', views.DetailView, name='detail'),
     url(r'^video/(?P<pk>[0-9]+)/$', views.VideoView, name='video'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
