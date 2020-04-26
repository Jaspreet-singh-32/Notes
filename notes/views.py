from django.shortcuts import render
from show.models import Data
from django.contrib import messages
def index(request):
    # first = First.objects.values('subject').distinct()
    # second = Second.objects.values('subject').distinct()
    # third = Third.objects.values('subject').distinct()
    # fourth = Fourth.objects.values('subject').distinct()
    # fifth = Fifth.objects.values('subject').distinct()
    # sixth = Sixth.objects.values('subject').distinct()
    # param = {'1st':first,'2nd':second,'3rd':third,'4th':fourth,'5th':fifth,'6th':sixth}

    data = Data.objects.values('subject').distinct()
    param = {'data':data}
    return render(request,'notes/index.html',param)

def search(request):
    s = request.GET.get('search')

    if len(s) > 50:
        search = Data.objects.none()
    else:
        search = Data.objects.filter(subject__istartswith=s).values('subject').distinct()
    if search.count() == 0:
        messages.info(request, "Your search did not match any document")
    param = {'data':search, 'search':s}
    return render(request, 'notes/search.html', param )  
    