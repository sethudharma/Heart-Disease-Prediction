from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.shortcuts import render
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
global scaler

import numpy as np
import cv2


from django.shortcuts import render

import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split


def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


def getPredictions(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, ECG_report, FH, FD,  alcohol, smoking , MT):
    model = pickle.load(open('KNN.pkl', 'rb'))
    prediction = model.predict(np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,   exang, oldpeak, slope, ca, thal, ECG_report, FH, FD,   alcohol, smoking , MT]]))
    return (prediction)

def result(request):
    age = int(request.GET['age'])
    sex = int(request.GET[ 'sex'])
    cp = int(request.GET[ 'cp'])
    trestbps = int(request.GET[ 'trestbps'])
    chol = int(request.GET[ 'chol'])
    fbs = int(request.GET[ 'fbs'])
    restecg = int(request.GET[ 'restecg'])
    thalach = int(request.GET[ 'thalach'])
    exang = int(request.GET[   'exang'])
    oldpeak = float(request.GET[ 'oldpeak'])
    slope = int(request.GET[ 'slope'])
    ca = int(request.GET[ 'ca'])
    thal = int(request.GET[ 'thal'])
    ECG_report = int(request.GET[ 'ECG_report'])
    FH = int(request.GET[ 'FH'])
    FD = int(request.GET[ 'FD'])
    alcohol = int(request.GET['alcohol'])
    smoking = int(request.GET[ 'smoking'])
    MT = int(request.GET[ 'MT'])
    result = getPredictions(age, sex, cp, trestbps, chol, fbs, restecg, thalach,  exang, oldpeak, slope, ca, thal, ECG_report, FH, FD,   alcohol, smoking , MT)
    if result.round()==1:
        res='Heart Disease'
    else:
        res='HEALTHY'
    return render(request, 'result.html', {'result': res})