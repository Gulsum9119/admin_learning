#from django.urls import path

from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),

    path(r'^course/$', views.courseListView.as_view(), name='course'),
    path(r'^course/(?P<pk>\d+)$', views.courseDetailView.as_view(), name='данные о курсе'),

    path(r'^teacher/$', views.teacherListView.as_view(), name='teacher'),
    path(r'^teacher/(?P<pk>\d+)$', views.teacherDetailView.as_view(), name='данные о преподавателе'),

  
  
]