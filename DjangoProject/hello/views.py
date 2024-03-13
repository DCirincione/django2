import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import ContactForm

def home(request):
    return render(request, "hello/home.html")
def about(request):
    return render(request, "hello/about.html")
def contact(request):
    return render(request, "hello/contact.html")

#Hello there
def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

# Define the 'play' view
def play(request):
    # Your logic here
    return render(request, 'hello/play.html')
def exhibits(request):
    # Your view logic here
    return HttpResponse("This is the Exhibits page.")
def calendar(request):
    # Your view logic for the calendar page
    return HttpResponse("This is the Calendar page.")
def progress(request):
    # Your view logic for the progress page
    return HttpResponse("This is the Progress page.")
def account(request):
    # Your view logic for the account page
    return HttpResponse("This is the Account page.")
def help(request):
    # Your view logic for the help page
    return HttpResponse("This is the Help page.")

#Home
def home(request):
    return render(request, "hello/home.html")

#About
def about(request):
    return render(request, "hello/about.html")

#Contact
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (you can add your own logic here)
            # For demonstration purposes, we'll just print the form data
            print(form.cleaned_data)
            # Redirect to a success page
            return redirect('contactsent')
    else:
        form = ContactForm()
    return render(request, 'hello/contact.html', {'form': form})


#Exhibits
def exhibits(request):
    return render(request, 'hello/exhibits.html')

#Calendar
def calendar(request):
    return redirect('https://glazermuseum.org/signatureevents/')

#Progress
def progress(request):
    return render(request, 'hello/progress.html')

#Account
def account(request):
    return render(request, 'hello/account.html')

#Help
def help(request):
    return render(request, 'hello/help.html')

