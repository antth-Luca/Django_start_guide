from django.urls import path
from .views import CreateCidadeView, ListCidadeView, EditCidadeView, DeleteCidadeView

urlpatterns = [
    path('list-cidade', ListCidadeView.as_view(), name='ListCidade'),
    path('create-cidade', CreateCidadeView.as_view(), name='CreateCidade'),
    path('edit-cidade/<int:pk>', EditCidadeView.as_view(), name='EditCidade'),
    path('delete-cidade/<int:pk>', DeleteCidadeView.as_view(), name='DeleteCidade'),
]
