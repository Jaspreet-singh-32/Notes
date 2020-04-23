from django.shortcuts import render
from show.models import First,Second,Third,Fourth,Fifth,Sixth

def index(request):
    first = First.objects.values('subject').distinct()
    second = Second.objects.values('subject').distinct()
    third = Third.objects.values('subject').distinct()
    fourth = Fourth.objects.values('subject').distinct()
    fifth = Fifth.objects.values('subject').distinct()
    sixth = Sixth.objects.values('subject').distinct()
    param = {'1st':first,'2nd':second,'3rd':third,'4th':fourth,'5th':fifth,'6th':sixth}
    return render(request,'notes/index.html',param)