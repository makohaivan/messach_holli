from django.shortcuts import render
from .models import Photo, Skill, Category, Service
from dashboard.models import Question, Testimonial
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.conf import settings

# Create your views here.
def home(request):
    photos = Photo.objects.all().select_related('category')[:10]
    skills = Skill.objects.all()[:3]
    categories = Category.objects.all()
    questions = Question.objects.all()
    testimonials = Testimonial.objects.all()
    service_list = Service.objects.all()[:4]
    
    context = {
        'photos':photos,
        'skills':skills,
        'categories':categories,
        'questions':questions,
        'testimonials':testimonials,
        'service_list':service_list
    }
    return render(request, 'portfolio/index.html', context)

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all().select_related('category')

    context = {
        'categories':categories,
        'photos':photos
    }

    return render(request, 'portfolio/gallery.html', context)

def about(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio/about.html' , {'skills':skills})

def contact(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'portfolio/contact.html', {'testimonials':testimonials})

def services(request):
    service_list = Service.objects.all()
    questions = Question.objects.all()
    
    context = {
       'service_list':service_list,
        'questions':questions
    }
    return render(request, 'portfolio/services.html', context)

@require_POST
def contact_form(request):
    try:
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Email the site admin
        send_mail(
            f"New Contact Form Submission: {subject}",
            f"From: {name} <{email}>\n\n{message}",
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        )
        
        return JsonResponse({'status': 'success', 'message': 'Your message has been sent. Thank you!'})
    
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)