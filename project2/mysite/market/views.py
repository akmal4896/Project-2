from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.

def index(request):
    return render(request, 'market/home.html')

class ItemDetailView(DetailView):
    model = Item

class ItemCreateView(CreateView):
    model = Item
    fields = ['title','price','description','date','category','condition','quantity']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
