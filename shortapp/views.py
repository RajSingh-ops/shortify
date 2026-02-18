from django.shortcuts import render,redirect
from .models import Url
def redirect_url(request,id):
    k=Url.objects.get(id=id)
    return redirect(k.url1)
def submit_url(request):
    urlq=request.POST['urlq']
    urll=Url(url1=urlq)
    urll.save()
    return render(request,'index.html',{"urln":"https://shortify.onrender.com/"+str(urll.id)})
def home(request):
    return render(request,'index.html')