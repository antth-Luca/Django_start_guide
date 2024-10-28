from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'Login_Logout/entrada.html'


@login_required
def SaidaView(request):
    logout(request)
    return redirect('Entrada')