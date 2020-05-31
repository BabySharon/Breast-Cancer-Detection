from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .forms import SignIn
from django.contrib import messages


def home(request):
    form = SignIn()
    return render(request,'index.html',{'form':form})

def addUser(request):
    # name = request.POST['name']
    # institution = request.POST['institution']
    # password = request.POST['password']
    form = SignIn(request.POST)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, f'Account Created for {user}!')
        return redirect('home')
    else:
        error_mssg = form.errors
        
        # error_non_field= form.non_field_errors
        # return render(request,'index.html',{'errors':error_mssg,'non_field':error_non_field})
        messages.warning(request,f'{form.errors}')
        return redirect('home')


def test(request):
    return render(request, 'services.html')
