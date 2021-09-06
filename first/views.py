from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import First
# Create your views here.


def view(request):
    query = First.objects.all()
    return render(request, 'view.html', {'data': query})


class Create(CreateView):
    model = First
    fields = ('title', 'content')
    template_name = 'add.html'
    success_url = '/first/create'
