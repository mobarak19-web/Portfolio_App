from django.contrib import admin
from .models import Skill, Project, Experience, Education, ContactMessage


# Register your models here.
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(ContactMessage)
