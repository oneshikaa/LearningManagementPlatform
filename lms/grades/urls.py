from django.urls import path,re_path

from . import views


app_name = 'grades'
urlpatterns = [
    path('list_grades/', views.list_grades, name='list_grades'),
    path('add_grade/', views.add_grade, name='add_grade'),
    re_path(r'^(?P<grade_id>\d+)/delete/$', views.delete_grade, name='delete_grade'),
    re_path(r'^(?P<grade_id>\d+)/update/$', views.update_grade, name='update_grade')

]
