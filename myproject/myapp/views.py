from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'index.html')
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     phone = request.POST['phone']
    #     date = request.POST['date']
    #     time = request.POST['time']
    #     people = request.POST['people']
    #     message = request.POST['message']

        
    #     if not name:
    #         messages.info(request, 'Please insert your name')
    #         return redirect('index')
    #     elif not email:
    #         messages.info(request, 'Please insert your email')
    #         return redirect('index')
    #     elif not phone:
    #         messages.info(request, 'Please insert your phone')
    #         return redirect('index')
    #     elif not date:
    #         messages.info(request, 'Please insert your date')
    #         return redirect('index') 
    #     elif not time:
    #         messages.info(request, 'Please insert the time')
    #         return redirect('index')
    #     elif not people:
    #         messages.info(request, 'Please insert number of people')
    #         return redirect('index')
    #     elif not message:
    #         messages.info(request, 'Please insert your message')
    #         return redirect('index')
    #     else:
    #         user = User.objects.create_user(name=name, email=email, phone=phone, date=date, time=time, people=people, message=message)
    #         user.save()
    #         # return HttpResponse('New contact created successfully')
    #         return redirect('index.html', {'books':books})
    
    # else:
    #     return render(request, 'index.html')
    # contacts = Contact.objects.all()
    

def book(request):
    books = Book.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        people = request.POST['people']
        message = request.POST['message']

        
        if not name:
            messages.info(request, 'Please insert your name')
            return redirect('index')
        elif not email:
            messages.info(request, 'Please insert your email')
            return redirect('index')
        elif not phone:
            messages.info(request, 'Please insert your phone')
            return redirect('index')
        elif not date:
            messages.info(request, 'Please insert your date')
            return redirect('index') 
        elif not time:
            messages.info(request, 'Please insert the time')
            return redirect('index')
        elif not people:
            messages.info(request, 'Please insert number of people')
            return redirect('index')
        elif not message:
            messages.info(request, 'Please insert your message')
            return redirect('index')
        else:
            user = User.objects.create_user(name=name, email=email, phone=phone, date=date, time=time, people=people, message=message)
            user.save()
            # return redirect('index')
            messages.info(request, "New booking created successfully")
            # return HttpResponse('New booking created successfully')
            return render(request, 'index.html', {'books':books})
    
    else:
        return redirect('index')


    