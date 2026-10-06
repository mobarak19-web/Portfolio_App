from django.shortcuts import render, redirect
from .models import Skill, Project, Experience, Education, ContactMessage
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, ContactForm

# Create your views here.

def Portfolio(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    
        
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()

    context = {
        'Skills': skills,
        'Projects': projects,
        'Experiences': experiences,
        'Educations': educations,
        'form': form,
    }
    return render(request, 'portfolio.html', context)


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard_view(request):
    messages = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'dashboard.html', {'messages': messages})


def resume_view(request):
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    return render(request, 'resume.html', {
        'experiences': experiences,
        'educations': educations,
        'skills': skills,
        'projects': projects
    })