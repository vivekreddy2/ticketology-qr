from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth as authe
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.conf.urls.static import static

def ask(request):
    return render(request, 'base.html')
def ans(request):
    sentence=request.POST.get('sentence')
    '''
    import tensor.py , take this string 'sentence' and call the function
    '''
    answer='return positive or negateive'
    print(sentence)
    return render(request, 'ans.html', {'answer':answer})
