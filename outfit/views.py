from django.shortcuts import render, HttpResponse, redirect
from dotenv import load_dotenv
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from user_auth.models import UserProfile
import os, random
load_dotenv()

def index(request):
  return render(request, 'index.html')

@login_required
def app(request):
    profile = request.user.profile

    if profile.measurements:
        return render(request, 'app.html', {'profile': profile})

    if request.method == 'POST':
        try:
            # Extracting form data from POST request
            print("post data: \n")
            print(request.POST)
            brand_preferences = request.POST.getlist('brand_preferences')
            price_range = int(request.POST.get('price_range', 500))  # default to 500 if not provided
            measurements = {
                'chest': request.POST.get('measurements[chest]'),
                'waist': request.POST.get('measurements[waist]'),
                'hips': request.POST.get('measurements[hips]'),
                'shoulders': request.POST.get('measurements[shoulders]'),
                'legs': request.POST.get('measurements[legs]')
            }
            preference = int(request.POST.get('preference', 3))  # default to 3 if not provided
            
            # Updating the profile instance
            profile.brand_preferences = brand_preferences
            profile.price_range = price_range
            profile.measurements = measurements
            profile.preference = preference
            profile.save()
            
            return render(request, 'app.html', {'profile': profile, 'message': "Success!"})
        except Exception as e:
            print(f"Error updating profile: {e}")
            return render(request, 'intro.html', {'message': "Error. Try Again."})
    else:
        return render(request, 'intro.html')  # Render an introductory form or page if not POST

def suggest(request):
  if request.method == 'GET':
    random_number = random.randint(1, 9)
    return render(request, 'alias/details.html', {'suggest': random_number})
# return render(request, 'alias/details.html')

def profile(request):
  return render(request, 'profile.html')

def cart(request):
  return render(request, 'cart.html')

def saved(request):
  return render(request, 'saved.html')

def handler500(request):
  return render(request, 'handler500.html', status=500)

def handler404(request, exception):
  return render(request, 'handler404.html', status=404)