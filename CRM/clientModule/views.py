from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Client
# Create your views here.


def index(request):
    clients_list = Client.objects.order_by('full_name')[:5]
    context = {'clients_list': clients_list}
    return render(request, 'clientModule/index.html', context)


def detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'clientModule/detail.html', {'client': client})


