from django.shortcuts import render
import os
from .forms import ContactForm

# Create your views here.



def home(request):
    return render(request, "app/home.html", {"active": "home"})


def design(request):
    folder1 = os.listdir("app/static/app/img/university/")
    folder2 = os.listdir("app/static/app/img/practice/")
    folder3 = os.listdir("app/static/app/img/bdosn/")
    print(folder1)
    return render(request, "app/design.html", {"active": "design", "folder1": folder1, "folder2": folder2, "folder3": folder3})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, "app/contact.html", {"active": "contact", 'form': form})