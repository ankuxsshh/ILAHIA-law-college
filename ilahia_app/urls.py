from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('courses', views.courses, name='courses'),
    path('gallery', views.gallery, name='gallery'),
    path('managements', views.managements, name='managements'),
    path('contact', views.contact, name='contact'),
    path('teacher', views.teacher, name='teacher'),
    path('teacher_single', views.teacher_single, name='teacher_single'),
    path('notice', views.notice, name='notice'),
    path('notice_single', views.notice_single, name='notice_single'),
    path('research', views.research, name='research'),
    path('scholarship', views.scholarship, name='scholarship'),
    path('course_details', views.course_details, name='course_details'),
    path('event_single', views.event_single, name='event_single'),
    path('blog_single', views.blog_single, name='blog_single'),
]