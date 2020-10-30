from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import CustomUserCreationForm

from .models import Room

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return JsonResponse({ 'message': 'Account created successfully' })
        else:
            return JsonResponse({ 'message': 'Invalid form' })
    else:
        return JsonResponse({ 'message': 'only POST allowed' })

def list_rooms(request):
    rooms = []
    for e in Room.objects.all():
        rooms.append({
          'name': e.name
        })
    return JsonResponse({ 'rooms': rooms })