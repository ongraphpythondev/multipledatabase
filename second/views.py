from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Second
# Create your views here.


def view(request):
    query = Second.objects.all()
    return render(request, 'view.html', {'data': query})


class Create(CreateView):
    model = Second
    fields = ('title', 'content')
    template_name = 'add.html'
    success_url = '/second/create'
