from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout as auth_logout

@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # user = authenticate(request, username=username, password=password)
            auth_login(request, form.get_user())
            return JsonResponse({"status": 1})
        else:
            return JsonResponse({"status": 0})

    else:
        form = AuthenticationForm()
        return JsonResponse({"status": 0})

@csrf_exempt
def logout(request):
    auth_logout(request)
    return JsonResponse({"status": 1})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return JsonResponse({"status": 1})
        else:
            form = UserCreationForm()
            return JsonResponse({"status": 0})
    
    else:
        return JsonResponse({"status": 0})