from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from market.models import Item

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #messages.success(request, f'Your account has been created! You can now log in!')
            return redirect('success')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html', {'form':form})

@login_required
def profile(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'users/profile.html', context)