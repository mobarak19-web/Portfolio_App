from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
        null=True,
        blank=True
        
    )
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True
    )
    description = models.TextField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"


class Skill(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='skills',
        null=True,
        blank=True
    )
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(
        help_text="Enter proficiency as a percentage (0-100)"
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='projects',
        null=True,
        blank=True
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies_used = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='experiences',
        null=True,
        blank=True
    )
    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    current_job = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"


class Education(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='educations',
        null=True,
        blank=True
     )
    degree = models.CharField(max_length=100)
    institution_name = models.CharField(max_length=200)
    passed_out_year = models.IntegerField()
    results = models.CharField(max_length=50)

    def __str__(self):
        return self.degree


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"