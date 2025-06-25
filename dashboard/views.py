from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Question, Testimonial
from .forms import FaqForm, TestimonialForm, PhotoForm, SkillForm
from portfolio.models import Photo

# Create your views here.
def custom_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard')  

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard:dashboard')  # Redirect after login
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'dashboard/login.html')

def custom_logout(request):
    logout(request)
    return redirect('portfolio:home')

@login_required(login_url='dashboard:login')
def dashboard(request):
    total_photos = Photo.objects.count()
    total_faqs = Question.objects.count()
    total_testimonials = Testimonial.objects.count()

    context = {
        'total_photos':total_photos,
        'total_faqs':total_faqs,
        'total_testimonials':total_testimonials 
    }

    return render(request, 'dashboard/dashboard.html', context)

def addFaq(request):
    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:dashboard') 
    else:
        form = FaqForm()
    return render(request, 'dashboard/addFaq.html', {'form': form})

def updateFaq(request, pk):
    question = get_object_or_404(Question, id=pk)

    if request.method == 'POST':
        form = FaqForm(request.POST, instance=question)

        if form.is_valid():
            form.save()
            return redirect('portfolio:home')
    else:
        form = FaqForm(instance=question)
        
    return render(request, 'dashboard/editFaq.html', {'form':form})
    
def deleteFaq(request, pk):
    question = Question.objects.get(id=pk)

    if request.method == 'POST':
        question.delete()
        return redirect('portfolio:home')
    
    return render(request, 'dashboard/deleteFaq.html', {'question': question})

# Testimonial views
def testimonialList(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'dashboard/testimonials.html', {'testimonials':testimonials})

def addTestimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:dashboard')
    else:
        form = TestimonialForm()
    return render(request, 'dashboard/addTestimonial.html', {'form':form})

def updateTestimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, id=pk)

    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('dashboard:dashboard')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(request, 'dashboard/editTestimonial.html', {'form':form})

def deleteTestimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, id=pk)

    if request.method == 'POST':
        testimonial.delete()
        return redirect('portfolio:home')
    return render(request, 'dashboard/deleteTestimonial.html', {'testimonial':testimonial})

# Photo views
def addPhoto(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio:home')
    else:
        form = PhotoForm()
    return render(request, 'dashboard/addPhoto.html', {'form':form})

# Skill view
def addSkill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio:about')
    else:
        form = SkillForm()
    return render(request, 'dashboard/addSkill.html', {'form':form})

