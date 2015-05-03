from django.conf.urls import patterns,url
from halkemi import views


urlpatterns = patterns('', url(r'^$', views.index, name='index'),
                           url(r'^signup$', views.signup, name='signup'),
                           url(r'^login$', views.signin, name='login'),
                           url(r'^signout$', views.signout, name='signout'),
                           url(r'^profile$', views.profile, name='profile'),
                           url(r'^edit-profile$', views.edit_profile, name='edit-profile'),
                           url(r'^edit-profile-picture$', views.edit_profile_picture, name='edit-profile-picture'),)