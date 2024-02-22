from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from website.models import Publication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse

# the import bellow is used to store values 
from .forms import PubForm



def indexPage(request):
    return render(request, 'website/index.html', {
        'newpubs':Publication.objects.order_by('date')[0:5]
    })
 
def writtersPage(request, writter_slug):
    return HttpReponse('Writters page') 
    
    """
    render(request, 'website/writterspage.html',{
        'writter' : Writter.objects.get(slug = writter_slug)
    })
    """    

def pubPage(request, pub_slug):
    pub = Publication.objects.filter(slug = pub_slug)[0]
    pub.view_number = pub.view_number + 1
    pub.save()
    
    return render(request, 'website/pub.html', {
        'pub' : pub
    }) 
    
def resultPage(request):
    return render(request, 'website/result.html', {
        'pubs' : Publication.objects.filter(title__contains = request.POST.get('search'))
    })
    
def aboutusPage(request):
    return render(request, 'website/aboutus.html')
    
def loginPage(request):
    return render(request, 'website/loginpage.html')
    
def checkLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username = username, password = password)
    
    if user is not None:
        return render(request, 'website/writterarea.html', {'pubs' : Publication.objects.all()})
    else:
        return render(request, 'website/loginpage.html', {'error' : 'You made some mistake. Try again.'}) 
        
    
def postPub(request):
    pub = Publication()
    pub.title = request.POST.get('title')
    pub.date = request.POST.get('date')
    pub.photo = request.POST.get('photo')
    pub.writter =  request.user
    pub.text = request.POST.get('text')
    
    pub.save()
    
    return HttpResponseRedirect(reverse('writterarea', args=()))

        
def writterArea(request):
    pubs = Publication.objects.filter(writter = request.user.id)
    
    form = PubForm()
    
    return render(request, 'website/wt_area.html', {'pubs' : pubs, 'form' : form})
    
def whatDo(request):
    whatdo = request.POST.get('whatdo')
    pubs = request.POST.get('pubs')
    
    Publication.objects.filter(title= request.POST.get('pubs')).delete()
    
    return HttpResponseRedirect(reverse('writterarea', args=()))
    
def updatePub(request, pub_id):
    if request.method == 'POST': 
        if form.is_valid():
            pub = Publication.objects.filter(writter = request.user)[0]
            pub.title = request.POST.get('title')
            pub.text = request.POST.get('text')
            pub.photo = request.POST.get('photo')
            pub.writter = request.user 
           
            pub.save()
       
        return HttpResponseRedirect(reverse('writterarea'))
    else: 
        pub = Publication.objects.get(id = pub_id)
        pubform = PubForm(instance = pub) 
       
        return render(request, 'website/updatepub.html', {'form' : pubform, 'pub_id' : pub_id})
        
