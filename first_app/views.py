from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView,UpdateView,DeleteView
from first_app import models
from django.urls import reverse_lazy
# Create your views here.


def index(req):
    return HttpResponse('Hello!...Its Home')


class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'first_app/index.html'


class MusicianDetails(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'first_app/musician_details.html'


class AddMusician(CreateView):
    fields = ('first_name', 'last_name', 'instrument')
    model = models.Musician
    template_name = 'first_app/add_musician.html'


class UpdateMusician(UpdateView):
    fields = ('first_name', 'last_name')
    model = models.Musician
    template_name = 'first_app/add_musician.html'


class DeleteMusician(DeleteView):
    context_object_name = 'musician'
    model = models.Musician
    success_url = reverse_lazy('first_app:home')
    template_name = 'first_app/delete_musician.html'