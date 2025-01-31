from django.shortcuts import render

"""
Views module for the Ilahia application.
This module contains the view functions for the Ilahia application.
"""


def index(request):
    """Render the index page."""
    return render(request, "index.html")


def about(request):
    """Render the about page."""
    return render(request, "about.html")


def courses(request):
    """Render the courses page."""
    return render(request, "courses.html")


def gallery(request):
    """Render the gallery page."""
    return render(request, "gallery.html")


def managements(request):
    """Render the managements page."""
    return render(request, "managements.html")


def contact(request):
    """Render the contact page."""
    return render(request, "contact.html")


def principal_desk(request):
    """Render the principal's desk page."""
    return render(request, "principal_desk.html")


def chairmans_desk(request):
    """Render the chairman's desk page."""
    return render(request, "chairmans_desk.html")


def admission_process(request):
    """Render the admission process page."""
    return render(request, "admission_process.html")


def fee_structure(request):
    """Render the fee structure page."""
    return render(request, "fee_structure.html")


def vicechairmans_desk(request):
    """Render the vice chairman's desk page."""
    return render(request, "vicechairmans_desk.html")


def administrator_desk(request):
    """Render the administrator's desk page."""
    return render(request, "administrator_desk.html")


def course_details(request):
    """Render the course details page."""
    return render(request, "course_details.html")


def academics(request):
    """Render the academics page."""
    return render(request, "academics.html")


def programs(request):
    """Render the programs page."""
    return render(request, "programs.html")


def facilities(request):
    """Render the facilities page."""
    return render(request, "facilities.html")


def achievements(request):
    """Render the achievements page."""
    return render(request, "achievements.html")


def moot_court_society(request):
    """Render the moot court society page."""
    return render(request, "moot_court_society.html")


def anti_ragging_cell(request):
    """Render the anti-ragging cell page."""
    return render(request, "anti_ragging_cell.html")


def women_cell(request):
    """Render the women cell page."""
    return render(request, "women_cell.html")


def complaint_cell(request):
    """Render the complaint cell page."""
    return render(request, "complaint_cell.html")


def legal_aid_clinic(request):
    """Render the legal aid clinic page."""
    return render(request, "legal_aid_clinic.html")
