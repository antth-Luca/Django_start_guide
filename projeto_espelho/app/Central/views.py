from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('Entrada')
    template_name = 'Central/home.html'
