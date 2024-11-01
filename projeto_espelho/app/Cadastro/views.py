from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

class CadastroUserView(CreateView):
    form_class = UserCreationForm
    template_name = 'Cadastro/cadastro.html'
    success_url = reverse_lazy('Entrada')
