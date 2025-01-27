from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('courses', views.courses, name='courses'),
    path('events', views.events, name='events'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('teacher', views.teacher, name='teacher'),
    path('teacher_single', views.teacher_single, name='teacher_single'),
    path('notice', views.notice, name='notice'),
    path('notice_single', views.notice_single, name='notice_single'),
    path('', views.research, name='research'),
    path('scholarship', views.scholarship, name='scholarship'),
    path('course_single', views.course_single, name='course_single'),
    path('event_single', views.event_single, name='event_single'),
    path('blog_single', views.blog_single, name='blog_single'),
]