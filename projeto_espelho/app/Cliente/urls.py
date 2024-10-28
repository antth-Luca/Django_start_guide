from django.urls import path
from .views import ListClienteView, CreateClienteView, EditClienteView, DeleteClienteView

urlpatterns = [
    path('list-cliente', ListClienteView.as_view(), name='ListCliente'),
    path('create-cliente', CreateClienteView.as_view(), name='CreateCliente'),
    path('edit-cliente/<int:pk>', EditClienteView.as_view(), name='EditCliente'),
    path('delete-cliente/<int:pk>', DeleteClienteView.as_view(), name='DeleteCliente'),
]
