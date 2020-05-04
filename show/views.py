from django.shortcuts import render,HttpResponse
from show.models import Data
from django.contrib import messages
from show.models import Contact
# Create your views here.
def all_notes(request):
    # first = First.objects.filter(subject=slug).values('title','any_message','id','trade','subject')
    # second = Second.objects.values('title','any_message','id','trade','subject')
    # third = Third.objects.values('title','any_message','id','trade','subject')
    # fourth = Fourth.objects.values('title','any_message','id','trade','subject')
    # fifth = Fifth.objects.values('title','any_message','id','trade','subject')
    # sixth = Sixth.objects.values('title','any_message','id','trade','subject')
    # param = {'1st':first,'2nd':second,'3rd':third,'4th':fourth,'5th':fifth,'6th':sixth,'sub':slug}
    if request.method == 'POST':
        all = request.POST.get('sub')
        l = all.split('->next->->')
        sub , trade , sem  = l[0] , l[1] , l[2]

        data = Data.objects.filter(subject=sub,trade=trade,sem=sem)
        param = {'data':data, 'sub':sub}
        return render(request, 'show/all_notes.html',param)
    else:
        return HttpResponse('404 - page not found')

def download(request ,slug):
    data = Data.objects.filter(id=slug)
    param = {'data':data}
    return render(request,'show/download.html',param)

# def search_notes(request):
#     # subject = request.GET.get()
#     title = request.GET.get('search')
#     search = Data.objects.filter(title__istartswith=title,).values('title','any_message','id','trade','subject','date','sem')
#     param = {'data':search}
#     # print(search)
#     # print('hello')
#     return render(request,'show/all_notes.html',param)


def contact(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        ph = request.POST.get('ph')
        msg = request.POST.get('msg')

        if len(name)<3 or len(email)<3 or (len(ph) < 10 or len(ph) > 13) or len(msg)<3:
            messages.warning(request,"Please fill all fields correctly")
        else:
            contact = Contact(name = name, email = email , phone = ph, message = msg)
            contact.save()
            messages.success(request,"Message received")

    return render(request,'show/contact.html')


def select_dept(request):
    sub = request.GET.get('all_notes')
    dept = Data.objects.filter(subject=sub).values('sem','trade','subject').distinct()
    param = {'data':dept}
    return render(request,'show/dept_and_sem.html',param)
    # return HttpResponse('depr and sem')
