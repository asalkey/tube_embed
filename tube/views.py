from django.http import HttpResponse
from django.shortcuts import render
from tube.models import Item


# Create your views here.

def index (request):
  return render(request, 'form.html')


def add(request):
    if request.GET['video']:
        vid = request.GET['video']
        return render(request, 'view.html',
            {'video': vid})
    else:
        return HttpResponse('Please submit a search term.')


# TODO: Add a list of all videos and route individually the view page

#def list (request):
  #videos = Item
  #t =loader.get_template('list.html')
  #c = Context({'videos':videos})
  #return HttpResponse(t.render(c))








