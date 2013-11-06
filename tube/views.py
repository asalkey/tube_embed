from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from tube.models import Item

class index(CreateView):
    model = Item
    fields = ['video']

class List(ListView):
    model = Item

class show(DetailView):
    model = Item










