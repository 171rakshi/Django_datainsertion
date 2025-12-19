from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
# Create your views here.
def insert_topic(request):
    tn=input('enter the topic name')
    TTO=Topic.objects.get_or_create(topic_name=tn)
    if TTO[1]:
         QLTO=Topic.objects.all()
         d={'QLTO':QLTO}
         return render(request,'display_topics.html',d)  
    else:
        return HttpResponse('Topic is already present')
    
def display_topics(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topics.html',d)
    
#retrieving pto object by filter
#retrieving by exclude ,it will retirieve objects which will not satisfy the condition
def insert_webpage(request):
    tn=input('enter the topic name')
    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        TO=LTO[0]
        na=input('enter the name')
        url=input('enter the url')
        TWO=WebPage.objects.get_or_create(topic_name=TO,name=na,url=url)
        if TWO[1]:
            QLWO=WebPage.objects.all()
            d={'QLWO':QLWO}
            return render(request,'display_webpages.html',d)    
        else:
            return HttpResponse('webpage is already exists')
    else:
        return HttpResponse('given topic is not present in parent(Topic) Table')
def display_webpages(request):
    QLWO=WebPage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpages.html',d)

def insert_accessrecord(request):
    wid=int(input('enter the id'))
    LWO=WebPage.objects.filter(id=wid)
    if LWO:
        LO=LWO[0]
        aut=input('enter the author')
        dt=input('enter the date ')
        LAO=AccessRecord.objects.get_or_create(name=LO,author=aut,date=dt)
        if LAO[1]:
            QLAO=AccessRecord.objects.all()
            d={'QLAO':QLAO}
            return render(request,'display_accessrecords.html',d)
        else:
            return HttpResponse('AccessRecord already exists')
    else:
        return HttpResponse('given webpage not presents')
    
def display_accessrecords(request):
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.all().order_by(Length('name').desc())   
    QLAO=AccessRecord.objects.all().order_by('name')
    QLAO=AccessRecord.objects.all().order_by('-name')
    QLAO=AccessRecord.objects.all()[::-1]
    QLAO=AccessRecord.objects.all()[:2:2]
    QLAO=AccessRecord.objects.all().order_by(Length('name'))
    QLAO=AccessRecord.objects.all(name_startswith='r')

    d={'QLAO':QLAO}
    return render(request,'display_accessrecords.html',d)

def update_webpage(request):
       #WebPage.objects.filter(name='msd').update(url='https:/msdhoni.com')
       #WebPage.objects.filter(topic_name='Cricket').update(name='ronaldo')
       #WebPage.objects.filter(topic_name='Cricket').update(name='ronaldo')
       #WebPage.objects.filter(topic_name='kabbadi').update(name='virat')
       #WebPage.objects.filter(topic_name='kabbadi').update(email='vk@gmail.com')
       #WebPage.objects.filter(topic_name='kabbadi').update(name='remo')
       #WebPage.objects.filter(url='https//:hardhik.in').update(name='hp')
       WebPage.objects.filter(url='https:/msdhoni.com').update(name='msd')
       #CTO=Topic.objects.get(topic_name='kabbadi')
       #WebPage.objects.update_or_create(name='ronaldo',defaults={'topic_name':CTO})
       QLWO=WebPage.objects.all()
       d={'QLWO':QLWO}
       return render(request,'display_webpages.html',d)
def delete_webpage(request):
    #WebPage.objects.filter(email='vk@gmail.com').delete()
    WebPage.objects.filter(name='msd').delete()
    QLWO=WebPage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpages.html',d)



def wish(request,n):
    return HttpResponse(f'Hi {n} how are you')