from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^profiles/(?P<profile_id>[-\w]+)/$', views.profiles, name='profiles'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url('create/',views.post,name ='post'),
    url('explore/',views.explore,name ='explore'),
    url('edit/',views.edit,name ='edit'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^vote/$', views.like, name='like'),
    url(r'^add/$', views.addComment, name='add'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)