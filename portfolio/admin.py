from django.contrib import admin
from .models import Category, Photo, Skill, Service

# Register your models here.
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Skill)
admin.site.register(Service)