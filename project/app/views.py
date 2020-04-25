from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Contacts

from django.utils import timezone


# Create your views here.

def home(request):
    contacts_items = Contacts.objects.all().order_by("-added_date")
    #print("-->", Contacts.objects.all())
    return render(request, 'home.html', {'contacts_items': contacts_items})


def add(request):
    # all_todo_items = Todo.objects.all()
    # print("\n\n\n -->",request.POST)
    # print(all_todo_items)
    # render(request, 'home.html', {'name': 'Add'}) #, {'item': all_todo_items})

    name = request.POST["text_name"] + request.POST["text_name"] + request.POST["text_name"] + request.POST["text_name"] 

    # Ver melhopr
    if name != "":
        create_obj = Contacts.objects.create(added_date=timezone.now(), text=name)

    return  HttpResponseRedirect("/")


def delete(request, contact_id):
    Contacts.objects.get(id=contact_id).delete()
    return HttpResponseRedirect("/")


def details(request, contact_id):
    #item = Contacts.objects.get(id=contact_id)
    #print("Contacts.objects.get(id=contact_id)=>  ", Contacts.objects.get(id=contact_id))
    return render(request, 'details.html'),# {'item': item})

