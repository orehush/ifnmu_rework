from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class FrontAppView(LoginRequiredMixin, TemplateView):
    template_name = 'front/index.html'
