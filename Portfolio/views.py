
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


# Create your views here.
def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all().order_by('-proficiency')
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    contact_form = ContactForm()

    context = {
        'page': 'Home',
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'educations': educations,
        'contact_form': contact_form,
    }

    return render(request, 'home.html', context)


# Portfolio view
def Portfolio(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('Portfolio')
    else:
        form = ContactForm()

    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'educations': educations,
        'form': form,
    }

    return render(request, 'portfolio.html', context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)

            messages.success(
                request,
                'Registration successful! You can now access your account.'
            )

            return redirect('login')
    else:
        form = RegistrationForm()

    return render(
        request,
        'register.html',
        {
            'page': 'User Registration',
            'form': form
        }
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(
                request,
                f'Welcome, {user.full_name or user.username}!'
            )

            return redirect('dashboard')
    else:
        form = LoginForm()

    return render(
        request,
        'login.html',
        {
            'page': 'User Login',
            'form': form
        }
    )


@login_required(login_url='login')
def dashboard_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    skills = Skill.objects.filter(user=request.user)
    educations = Education.objects.filter(user=request.user)
    experiences = Experience.objects.filter(user=request.user)
    projects = Project.objects.filter(user=request.user)
    messages_list = ContactMessage.objects.all()

    context = {
        'page': 'Dashboard',
        'profile': profile,
        'skills': skills,
        'educations': educations,
        'experiences': experiences,
        'projects': projects,
        'messages_list': messages_list,
    }

    return render(request, 'dashboard.html', context)


def resume_view(request):
    profile = Profile.objects.first()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()

    context = {
        'page': 'Resume',
        'profile': profile,
        'experiences': experiences,
        'educations': educations,
        'skills': skills,
        'projects': projects
    }

    return render(request, 'resume.html', context)


@login_required(login_url='login')
def update_profile(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your profile details have been saved successfully!.'
            )
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)

    return render(
        request,
        'update_profile.html',
        {
            'page': 'Update Profile',
            'form': form
        }
    )


@login_required(login_url='login')
def change_pass(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Password updated successfully!'
            )
            return redirect('dashboard')
    else:
        form = ChangePasswordForm(request.user)

    return render(
        request,
        'change_pass.html',
        {
            'page': 'Change Password',
            'form': form
        }
    )


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('user_login')


# ============================================================
# Skill Management Views
# ============================================================

@login_required(login_url='login')
def skill_create(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)

        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()

            messages.success(
                request,
                'Skill added successfully!'
            )

            return redirect('skill_list')
    else:
        form = SkillForm()

    return render(
        request,
        'skill_create.html',
        {
            'page': 'Create Skill',
            'form': form
        }
    )


@login_required(login_url='login')
def skill_list(request):
    skills = Skill.objects.filter(user=request.user)

    return render(
        request,
        'skill_list.html',
        {
            'page': 'Skill List',
            'skills': skills
        }
    )


@login_required(login_url='login')
def skill_update(request, id):
    skill = get_object_or_404(
        Skill,
        id=id,
        user=request.user
    )

    if request.method == 'POST':
        form = SkillForm(
            request.POST,
            instance=skill
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Skill update completed successfully!'
            )

            return redirect('skill_list')
    else:
        form = SkillForm(instance=skill)

    return render(
        request,
        'skill_update.html',
        {
            'page': 'Update Skill',
            'form': form
        }
    )


@login_required(login_url='login')
def skill_delete(request, id):
    skill = get_object_or_404(
        Skill,
        id=id,
        user=request.user
    )

    skill.delete()

    messages.success(
        request,
        'Skill removed successfully!'
    )

    return redirect('skill_list')


# ============================================================
# Education Management Views
# ============================================================

@login_required(login_url='login')
def education_create(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)

        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user
            education.save()

            messages.success(
                request,
                'Education information added successfully!.'
            )

            return redirect('education_list')
    else:
        form = EducationForm()

    return render(
        request,
        'education_create.html',
        {
            'page': 'Create Education',
            'form': form
        }
    )


@login_required(login_url='login')
def education_list(request):
    educations = Education.objects.filter(
        user=request.user
    )

    return render(
        request,
        'education_list.html',
        {
            'page': 'Education List',
            'educations': educations
        }
    )


@login_required(login_url='login')
def education_update(request, id):
    education = get_object_or_404(
        Education,
        id=id,
        user=request.user
    )

    if request.method == 'POST':
        form = EducationForm(
            request.POST,
            instance=education
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Education has been updated successfully!'
            )

            return redirect('education_list')
    else:
        form = EducationForm(instance=education)

    return render(
        request,
        'education_update.html',
        {
            'page': 'Update Education',
            'form': form
        }
    )


@login_required(login_url='login')
def education_delete(request, id):
    education = get_object_or_404(
        Education,
        id=id,
        user=request.user
    )

    education.delete()

    messages.success(
        request,
        'Education removed successfully!.'
    )

    return redirect('education_list')


# ============================================================
# Experience Management Views
# ============================================================

@login_required(login_url='login')
def experience_create(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)

        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()

            messages.success(
                request,
                'Experience information added successfully!.'
            )

            return redirect('experience_list')
    else:
        form = ExperienceForm()

    return render(
        request,
        'experience_create.html',
        {
            'page': 'Create Experience',
            'form': form
        }
    )


@login_required(login_url='login')
def experience_list(request):
    experiences = Experience.objects.filter(
        user=request.user
    )

    return render(
        request,
        'experience_list.html',
        {
            'page': 'Experience List',
            'experiences': experiences
        }
    )


@login_required(login_url='login')
def experience_update(request, id):
    experience = get_object_or_404(
        Experience,
        id=id,
        user=request.user
    )

    if request.method == 'POST':
        form = ExperienceForm(
            request.POST,
            instance=experience
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Experience updated successfully!.'
            )

            return redirect('experience_list')
    else:
        form = ExperienceForm(instance=experience)

    return render(
        request,
        'experience_update.html',
        {
            'page': 'Update Experience',
            'form': form
        }
    )


@login_required(login_url='login')
def experience_delete(request, id):
    experience = get_object_or_404(
        Experience,
        id=id,
        user=request.user
    )

    experience.delete()

    messages.success(
        request,
        'Experience removed successfully!.'
    )

    return redirect('experience_list')


# ============================================================
# Project Management Views
# ============================================================

@login_required(login_url='login')
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()

            messages.success(
                request,
                'Project information added successfully!.'
            )

            return redirect('project_list')
    else:
        form = ProjectForm()

    return render(
        request,
        'project_create.html',
        {
            'page': 'Create Project',
            'form': form
        }
    )


@login_required(login_url='login')
def project_list(request):
    projects = Project.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'project_list.html',
        {
            'page': 'Project List',
            'projects': projects
        }
    )


@login_required(login_url='login')
def project_update(request, id):
    project = get_object_or_404(
        Project,
        id=id,
        user=request.user
    )

    if request.method == 'POST':
        form = ProjectForm(
            request.POST,
            request.FILES,
            instance=project
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Project information updated successfully!.'
            )

            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)

    return render(
        request,
        'project_update.html',
        {
            'page': 'Update Project',
            'form': form
        }
    )


@login_required(login_url='login')
def project_delete(request, id):
    project = get_object_or_404(
        Project,
        id=id,
        user=request.user
    )

    project.delete()

    messages.success(
        request,
        'Project removed successfully!.'
    )

    return redirect('project_list')


# ============================================================
# Contact Message Management Views
# ============================================================

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Your message has been delivered successfully!'
            )

            return redirect('contact')
    else:
        form = ContactForm()

    return render(
        request,
        'contact.html',
        {
            'page': 'Contact',
            'form': form
        }
    )


@login_required(login_url='login')
def contact_messages(request):
    messages_list = ContactMessage.objects.all()

    return render(
        request,
        'contact_messages.html',
        {
            'page': 'Contact Messages',
            'messages_list': messages_list
        }
    )


@login_required(login_url='login')
def contact_message_detail(request, id):
    message = get_object_or_404(
        ContactMessage,
        id=id
    )

    message.is_read = True
    message.save()

    return render(
        request,
        'contact_message_detail.html',
        {
            'page': 'Contact Message Detail',
            'message': message
        }
    )


@login_required(login_url='login')
def contact_message_delete(request, id):
    message = get_object_or_404(
        ContactMessage,
        id=id
    )

    message.delete()

    messages.success(
        request,
        'Message removed successfully.'
    )

    return redirect('contact_messages')

# @login_required(login_url='login')
# def manage_portfolio(request):
#     profile, _ = Profile.objects.get_or_create(user=request.user)

#     skills = Skill.objects.filter(user=request.user)
#     projects = Project.objects.filter(user=request.user)
#     educations = Education.objects.filter(user=request.user)
#     experiences = Experience.objects.filter(user=request.user)

#     return render(request, 'manage_portfolio.html', {
#         'page': 'Manage Portfolio',
#         'profile': profile,
#         'skills': skills,
#         'projects': projects,
#         'educations': educations,
#         'experiences': experiences,
#     })