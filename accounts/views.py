from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET

from accounts.forms import CreateUserForm
from accounts.models import User

# Create your views here.
@require_http_methods(['GET'])
def profile(request):
    return render(request, 'registration/profile.html')




@require_http_methods(['GET', 'POST'])
def create_new_account(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():

            User.objects.create_user(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    email=form.cleaned_data['email'],
                    discription=form.cleaned_data['discription']
                  )
            return redirect(reverse('login'))


    elif request.method == "GET":
        form = CreateUserForm()
        return render(request, 'registration/create_new_account_form.html', {
                'form': form,
            })

