from django.urls import path
from .views import CadastroUserView

urlpatterns = [
    path('cadastrar/', CadastroUserView.as_view(), name='CadastroUser'),
]