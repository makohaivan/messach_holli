from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Auto-generate slug if empty
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='photos')
    image = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    skill_level = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    def __str__(self):
        return self.title

class Service(models.Model):
    ICON_CHOICES = [
    ('bi bi-camera', 'Camera'),
    ('bi bi-heart-fill', 'Heart'),
    ('bi bi-calendar-event', 'Calendar'),
    ('bi bi-geo-alt', 'location'),
    ('bi bi-person-circle', 'person'),
    ('bi bi-sliders', 'sliders'),
    ('bi bi-camera-reels-fill', 'camera reels'),
    ('bi bi-camera-video', 'drone'),
    ('bi bi-box-seam', 'box')
   
]
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=100, choices=ICON_CHOICES)

    def __str__(self):
        return self.title