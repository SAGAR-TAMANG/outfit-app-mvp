from django.shortcuts import render, HttpResponse, redirect
from dotenv import load_dotenv
import os, random
load_dotenv()

def index(request):
  return render(request, 'index.html')

from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

@login_required
def app(request):
  profile = request.user.profile  # Access the related profile
  if request.method == 'POST':
      form = UserProfileForm(request.POST, instance=profile)
      if form.is_valid():
          form.save()
          return redirect('profile_success')  # Redirect to a success or dashboard page
  else:
      form = UserProfileForm(instance=profile)

  return render(request, 'app.html', {'form': form})

def handler500(request):
  return render(request, 'handler500.html', status=500)

def handler404(request, exception):
  return render(request, 'handler404.html', status=404)

