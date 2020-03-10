from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.utils.text import gettext_lazy as _

from .forms import ReworkCreateForm
from .models import Rework


class ReworkCreateView(CreateView):
    form_class = ReworkCreateForm
    template_name = 'subject/rework/create.html'

    def get_success_url(self):
        return reverse('rework-list')

    def get_form_kwargs(self):
        kwargs = super(ReworkCreateView, self).get_form_kwargs()
        kwargs['student'] = self.request.user
        return kwargs

    def form_valid(self, form):
        messages.success(
            self.request,
            _('Request for rework successfully registered')
        )
        return super(ReworkCreateView, self).form_valid(form)


class ReworkListView(ListView):
    queryset = Rework.objects.all()
    template_name = 'subject/rework/list.html'
    context_object_name = 'reworks'

    def get_queryset(self):
        # TODO filter by user type
        return self.queryset
