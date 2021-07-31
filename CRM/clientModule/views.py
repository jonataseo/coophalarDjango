from django.shortcuts import render

from .models import Client
# Create your views here.


def index(request):
    clients_list = Client.objects.order_by('full_name')[:5]
    context = {'clients_list': clients_list}
    return render(request, 'clientModule/index.html', context)


def detail(request, client_id):
    return HttpResponse("Client %s" % client_id)


