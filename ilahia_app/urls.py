from django.urls import path
from . import views

"""
URLs module for the Ilahia application.
This module defines the URL patterns for the Ilahia application.
"""

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("courses", views.courses, name="courses"),
    path("gallery", views.gallery, name="gallery"),
    path("managements", views.managements, name="managements"),
    path("contact", views.contact, name="contact"),
    path("principal_desk", views.principal_desk, name="principal_desk"),
    path("chairmans_desk", views.chairmans_desk, name="chairmans_desk"),
    path("admission_process", views.admission_process, name="admission_process"),
    path("fee_structure", views.fee_structure, name="fee_structure"),
    path("vicechairmans_desk", views.vicechairmans_desk, name="vicechairmans_desk"),
    path("administrator_desk", views.administrator_desk, name="administrator_desk"),
    path("course_details", views.course_details, name="course_details"),
    path("academics", views.academics, name="academics"),
    path("programs", views.programs, name="programs"),
    path("facilities", views.facilities, name="facilities"),
    path("achievements", views.achievements, name="achievements"),
    path("moot_court_society", views.moot_court_society, name="moot_court_society"),
    path("anti_ragging_cell", views.anti_ragging_cell, name="anti_ragging_cell"),
    path("women_cell", views.women_cell, name="women_cell"),
    path("complaint_cell", views.complaint_cell, name="complaint_cell"),
    path("legal_aid_clinic", views.legal_aid_clinic, name="legal_aid_clinic"),
]
