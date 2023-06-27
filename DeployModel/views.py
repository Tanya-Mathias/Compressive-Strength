from django.http import HttpResponse
from django.shortcuts import render
import joblib
def home(request):
    return render(request,"home.html")
def result(request):
    rf_random=joblib.load('finalisedmodel.sav')
    lst=[]
    lst.append(request.GET['Fly ash'])
    lst.append(request.GET['Cement'])
    lst.append(request.GET['Slag'])
    lst.append(request.GET['Water'])
    lst.append(request.GET['SP'])
    lst.append(request.GET['Coarse Aggr.'])
    lst.append(request.GET['Fine Aggr.'])
    ans1=rf_random.predict([lst])
    ans=ans1[0]
    return render(request,"result.html",{'ans':ans})