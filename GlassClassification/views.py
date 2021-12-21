from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request,"home.html")

def result(request):
    cls = joblib.load('final_model.sav')

    li = []
    li.append(request.GET['RI'])
    li.append(request.GET['Na'])
    li.append(request.GET['Mg'])
    li.append(request.GET['Al'])
    li.append(request.GET['Si'])
    li.append(request.GET['K'])
    li.append(request.GET['Ca'])
    li.append(request.GET['Ba'])
    li.append(request.GET['Fe'])

    ans = cls.predict([li])

    return render(request,"result.html",{'ans':ans,'li':li})
