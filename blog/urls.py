from django.conf.urls import url
from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'posts',views.PostApiView)


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'base/',views.BaseView.as_view(),name='base-view'),
    url(r'api/', include(router.urls))
]



