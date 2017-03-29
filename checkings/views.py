from django.views.generic import ListView, DetailView, UpdateView

from .models import CheckModel


class CheckingsListView(ListView):
    model = CheckModel
    context_object_name = 'dich_list'
    template_name = 'checkings/change-list.html'

    def get_context_data(self, **kwargs):
        context = super(CheckingsListView, self).get_context_data(**kwargs)
        context['title'] = 'Checking list'
        return context


class CheckingsDetailView(DetailView):
    model = CheckModel
    template_name = 'checkings/change-detail.html'


