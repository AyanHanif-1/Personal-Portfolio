from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Skills , Projects , Contact

def home(request):
    skills = Skills.objects.all()

    return render(request, "portfolio_app/home.html", {
        "skills": skills,
    })

from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and message:

            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('contact')

        else:
            messages.error(request, 'Failed to send message. Please fill out all required fields.')

    return render(request, 'portfolio_app/contact.html')


def projects(request):
    projects = Projects.objects.all()

    return render(request, "portfolio_app/projects.html", {
        "projects": projects,
    })
