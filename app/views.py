from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import * 

def djangoForm(request):
    form=NameForm()
    if request.method=='POST':
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            name=form_data.cleaned_data['name']
            #age=form_data.cleaned_data['age']
            #email=form_data.cleaned_data['email']
            #url=form_data.cleaned_data['url']
            #date=form_data.cleaned_data['date']
            #date1=form_data.cleaned_data['date1']
            #time=form_data.cleaned_data['time']
            password=form_data.cleaned_data['password']
            address=form_data.cleaned_data['address']
            gender=form_data.cleaned_data['gender']
            course=form_data.cleaned_data['course']
            #d={'name':name,'age':age,'email':email,'url':url,'date':date,'date1':date1,'time':time}
            d1={'name':name,'password':password,'address':address,'gender':gender,'course':course}
            return render(request,'formdata.html',context=d1)
            

    return render(request,'temp1.html',context={'form':form})