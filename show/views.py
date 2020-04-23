from django.shortcuts import render
from .models import First,Second,Third,Fourth,Fifth,Sixth
# Create your views here.
def all_notes(request,slug):
    first = First.objects.filter(subject=slug).values('title','any_message','id','trade','subject')
    second = Second.objects.values('title','any_message','id','trade','subject')
    third = Third.objects.values('title','any_message','id','trade','subject')
    fourth = Fourth.objects.values('title','any_message','id','trade','subject')
    fifth = Fifth.objects.values('title','any_message','id','trade','subject')
    sixth = Sixth.objects.values('title','any_message','id','trade','subject')
    param = {'1st':first,'2nd':second,'3rd':third,'4th':fourth,'5th':fifth,'6th':sixth,'sub':slug}
    return render(request,'show/all_notes.html',param)

def selected(request,slug):
    first = First.objects.filter(id=slug)
    second = Second.objects.filter(id=slug)
    third = Third.objects.filter(id=slug)
    fourth = Fourth.objects.filter(id=slug)
    fifth = Fifth.objects.filter(id=slug)
    sixth = Sixth.objects.filter(id=slug)
    param = {'1st':first,'2nd':second,'3rd':third,'4th':fourth,'5th':fifth,'6th':sixth}
    
    return render(request,'show/subjects.html',param)