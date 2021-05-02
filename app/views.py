from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import * 

def djangoForm(request):
    form=NameForm()
    if request.method=='POST':
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            #return HttpResponse(str(form_data.cleaned_data))
            return HttpResponse(form_data.cleaned_data['name'])
    return render(request,'temp1.html',context={'form':form})