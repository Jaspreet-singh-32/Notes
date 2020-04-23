from django.shortcuts import render
from .models import First,Second,Third,Fourth,Fifth,Sixth
# Create your views here.
def all_notes(request,slug):
    first = First.objects.filter(subject=slug).values('title')
    second = Second.objects.values('title').distinct()
    third = Third.objects.values('title').distinct()
    fourth = Fourth.objects.values('title').distinct()
    fifth = Fifth.objects.values('title').distinct()
    sixth = Sixth.objects.values('title').distinct()
    param = {'1st':first,'2nd':second,'3rd':third,'4th':fourth,'5th':fifth,'6th':sixth,'sub':slug}
    return render(request,'show/all_notes.html',param)