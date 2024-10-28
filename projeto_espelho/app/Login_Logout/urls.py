from django.urls import path
from .views import CustomLoginView, SaidaView

urlpatterns = [
    path('entrar', CustomLoginView.as_view(), name='Entrada'),
    path('sair', SaidaView, name='Saida'),
]
