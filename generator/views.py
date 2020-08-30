from django.shortcuts import render
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    listwords = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        listwords.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('numbers'):
        listwords.extend('1234567890')

    if request.GET.get('specialchars'):
        listwords.extend('!@#$%^&*()')

    thepassword=''
    for x in range(length):
        thepassword += random.choice(listwords)
        
    return render(request,'generator/password.html', {'thepassword': thepassword})

def about(request):
    return render(request, 'generator/about.html')