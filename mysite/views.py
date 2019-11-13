from django.shortcuts import get_object_or_404,render
from mysite.models import Note
# Create your views here.


def index(request,category=''):
    if category == '':
        nList = Note.objects.filter(nIsPublic=True).order_by('-nUpdateTime')
    elif category == 'pri':
        nList = Note.objects.filter(nIsPublic=False).order_by('-nUpdateTime')
    else:
        nList = Note.objects.filter(nCategory=category,nIsPublic=True).order_by('-nUpdateTime')
    return render(request, 'mysite/index.html', {'nList': nList,'category': category, 'isIndex': ''})


def detail(request,nId):
    note = get_object_or_404(Note, pk=nId)
    note.nView += 1
    note.save()
    return render(request,'mysite/detail.html',{'note':note,'isIndex':'wrap_detail'})


def about(request):
    return render(request, 'mysite/about.html')