from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente

# Create your views here.
class ListClienteView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('Entrada')
    model = Cliente
    template_name = 'Cliente/list-cliente.html'
    context_object_name = 'clientes'


class CreateClienteView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('Entrada')
    model = Cliente
    fields = '__all__'
    template_name = 'Cliente/create-cliente.html'
    success_url = reverse_lazy('ListCliente')


class EditClienteView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('Entrada')
    model = Cliente
    fields = '__all__'
    template_name = 'Cliente/edit-cliente.html'
    success_url = reverse_lazy('ListCliente')


class DeleteClienteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('Entrada')
    model = Cliente
    template_name = 'Cliente/delete-cliente.html'
    success_url = reverse_lazy('ListCliente')
