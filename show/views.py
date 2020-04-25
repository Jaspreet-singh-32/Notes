from django.shortcuts import render,HttpResponse
from show.models import Data
# Create your views here.
def all_notes(request):
    # first = First.objects.filter(subject=slug).values('title','any_message','id','trade','subject')
    # second = Second.objects.values('title','any_message','id','trade','subject')
    # third = Third.objects.values('title','any_message','id','trade','subject')
    # fourth = Fourth.objects.values('title','any_message','id','trade','subject')
    # fifth = Fifth.objects.values('title','any_message','id','trade','subject')
    # sixth = Sixth.objects.values('title','any_message','id','trade','subject')
    # param = {'1st':first,'2nd':second,'3rd':third,'4th':fourth,'5th':fifth,'6th':sixth,'sub':slug}
    sub = request.GET.get('all_notes')
    data = Data.objects.filter(subject=sub).values('title','any_message','id','trade','subject','date','sem')
    param = {'data':data, 'sub':sub}
    return render(request, 'show/all_notes.html',param)

def download(request ,slug):
    # first = First.objects.filter(id=slug)
    # second = Second.objects.filter(id=slug)
    # third = Third.objects.filter(id=slug)
    # fourth = Fourth.objects.filter(id=slug)
    # fifth = Fifth.objects.filter(id=slug)
    # sixth = Sixth.objects.filter(id=slug)
    # param = {'1st':first,'2nd':second,'3rd':third,'4th':fourth,'5th':fifth,'6th':sixth}
    data = Data.objects.filter(id=slug)
    param = {'data':data}
    return render(request,'show/download.html',param)

def search_notes(request):
    # subject = request.GET.get()
    title = request.GET.get('search')
    search = Data.objects.filter(title__istartswith=title,).values('title','any_message','id','trade','subject','date','sem')
    param = {'data':search}
    # print(search)
    # print('hello')
    return render(request,'show/all_notes.html',param)