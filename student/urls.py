from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add_student', views.add_student, name='add_student'),
    path('all_student', views.all_student, name='all_student'),
    path('remove_student', views.remove_student, name='remove_student')

]
