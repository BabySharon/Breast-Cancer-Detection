from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .forms import SignIn, PatientForm
from django.contrib import messages
from .apps import TestConfig
import torch
import json
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image
from io import StringIO


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


# def login(request):


def test(request):
    form = PatientForm()
    print("reched get")
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            img = str(request.FILES['testfile'])
            with open('C:\\Users\\lenovo\\Desktop\\project\\Breast-Cancer-Detection\\django-project\\test\\cat_to_name.json', 'r') as f:
                cat_to_name = json.load(f)
            # testobj = TestConfig(test,None)
            loaded_model, class_to_idx = TestConfig.load_checkpoint('C:\\Users\\lenovo\\Downloads\\new_152_checkpoint.pt')
            TestConfig.idx_to_class = { v : k for k,v in class_to_idx.items()}
            p, c = TestConfig.predict('media\\images\\' +img, loaded_model)
            print(cat_to_name)
            TestConfig.view_classify(img, p, c, cat_to_name)
           

            # form = PatientForm()
        else:
            print(form.errors)
    context = {'form':form}    
    return render(request, 'services.html',context)

    