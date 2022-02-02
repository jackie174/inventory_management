from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import *

from .forms import *


def index(request):
    return render(request, 'inv/index.html')

def display_volunteers(request):
    items = Volunteers.objects.all()
    context = {
        'items': items,
        'header': 'volunteers',
    }
    return render(request, 'inv/index.html', context)


def display_participates(request):
    items = Participates.objects.all()
    context = {
        'items': items,
        'header': 'participates',
    }
    return render(request, 'inv/index.html', context)



def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'inv/add_new.html', {'form' : form})


def add_volunteer(request):
    return add_item(request, VolunteerForm)


def add_participate(request):
    return add_item(request, ParticipateForm)




def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'inv/edit_item.html', {'form': form})



def edit_volunteer(request, pk):
    return edit_item(request, pk, Volunteers, VolunteerForm)


def edit_participate(request, pk):
    return edit_item(request, pk, Participates, ParticipateForm)


def delete_volunteer(request, pk):

    template = 'inv/index.html'
    Volunteers.objects.filter(id=pk).delete()

    items = Volunteers.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_participate(request, pk):

    template = 'inv/index.html'
    Participates.objects.filter(id=pk).delete()

    items = Participates.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)
