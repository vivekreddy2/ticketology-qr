from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth as authe
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.conf.urls.static import static
import pyrebase


config = {

    'apiKey': "AIzaSyA520VBeHVrhEF1hpJ13S2D1ZD94TlyNOE",
    "authDomain": "software-engineering-6e9a7.firebaseapp.com",
    'databaseURL': "https://software-engineering-6e9a7.firebaseio.com",
    'projectId': "software-engineering-6e9a7",
    'storageBucket': "software-engineering-6e9a7.appspot.com",
    'messagingSenderId': "329135496498"
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

def ask(request):
    return render(request, 'base.html')


def ans(request):
    sentence=request.POST.get('sentence')
    print(sentence)
    db.child('boarded').push(sentence)
    print(sentence)
    return render(request, 'ans.html')
