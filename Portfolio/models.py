from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Enter proficiency as a percentage (0-100)")

    def __str__(self):
        return self.name
    

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies_used = models.CharField(max_length=200)
    # project_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Experience(models.Model):
    company_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.role} at {self.company_name}"
    
    
class Education(models.Model):
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