from django.views.generic import ListView, DetailView, UpdateView

from .models import CheckModel


class CheckingsList(ListView):
    model = CheckModel
    template_name = 'checkings/change-list.html'


