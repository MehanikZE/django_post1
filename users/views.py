from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from .forms import LoginUserForm


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'fff.html'
    extra_context = {'title': "AVTOR"}

# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user:
#                 login(request, user)
#                 # return HttpResponseRedirect(reverse('main'))
#     else:
#         # return render(request, 'fff.html')
#         form = LoginUserForm()
#     return render(request, 'fff.html', {'form': form})
    # return HttpResponseRedirect(reverse(viewname='addpost'))