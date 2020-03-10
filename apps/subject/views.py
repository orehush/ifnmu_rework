from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, ListView, TemplateView
from django.utils.text import gettext_lazy as _

from .forms import ReworkCreateForm
from .models import Rework


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'base.html'


class ReworkCreateView(LoginRequiredMixin, CreateView):
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


class ReworkListView(LoginRequiredMixin, ListView):
    queryset = Rework.objects.all()
    template_name = 'subject/rework/list.html'
    context_object_name = 'reworks'

    def get_queryset(self):
        user = self.request.user
        if user.is_student():
            return self.queryset.filter(student=user)
        if user.is_teacher():
            return self.queryset.filter(subject__department=user.department)
        if user.is_officer() or user.is_superuser:
            return self.queryset
        return self.queryset.none()
