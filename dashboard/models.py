from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question
    

class Testimonial(models.Model):
    title = models.CharField(max_length=200)
    description1 = models.TextField()
    description2 = models.TextField(blank=True)
    image = models.ImageField(upload_to='testimonials/')
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)

    def __str__(self):
        return self.title