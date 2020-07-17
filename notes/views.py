from django.shortcuts import render
from django.contrib import messages
from show.models import Data

def index(request):

    data = Data.objects.values('subject').distinct()
    d = Data.objects.all()
    print(d)
    param = {'data':data}
    return render(request,'notes/index.html',param)

def search(request):
    s = request.GET.get('search')

    if len(s) > 50:
        search = Data.objects.none()
    else:
        search = Data.objects.filter(subject__istartswith=s).values('subject').distinct()
        # searchdept = Data.objects.filter(trade__icontains=s)
        # search = searchsub.union(searchdept)
    if search.count() == 0:
        messages.info(request, "Your search did not match any document")
    param = {'data':search, 'search':s}
    return render(request, 'notes/search.html', param )  
    