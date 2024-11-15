from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    about = About.objects.first()
    services = Service.objects.all()
    projects = Project.objects.all()
    education = Education.objects.all()
    contact = Contact.objects.all()
    skills = Skill.objects.all()
    link = Link.objects.all()
    experience = Experience.objects.all()
    certificate = Certificate.objects.all()
    certificate_category = Category_Certificate.objects.all()

    context = {
        "about": about,
        "services": services,
        "projects": projects,
        "education": education,
        "contact": contact,
        "skills": skills,
        "link": link,
        "experience": experience,
        "certificate": certificate,
        "certificate_category": certificate_category,
    }
    return render(request, "index.html", context)


def contact(request):
    if request.method == "POST":
        contact_name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            contact_name=contact_name, email=email, subject=subject, message=message
        )

        return render(request, "index.html")
