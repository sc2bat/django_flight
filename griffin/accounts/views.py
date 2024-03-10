from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout as auth_logout
from .forms import MyUserCreationForm
from rest_framework.parsers import JSONParser
from .models import Users
from .serializers import UsersSerializer

@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())

            auth_email = form.get_user().email

            try:
                query = {}
                if auth_email is not None:
                    query['email'] = auth_email

                if query:
                    obj = Users.objects.filter(**query)
                    serializer = UsersSerializer(obj, many=True)
                    return JsonResponse(serializer.data, safe=False)
                else:
                    return JsonResponse({"status": 0, "case": 'none user'})

            except Users.DoesNotExist:
                return JsonResponse({"status": 0, "case": 'none user'}, safe=False)

            # return JsonResponse({"username": form.get_user().username, "email": form.get_user().email})
        else:
            return JsonResponse({"status": 0, "case": form.errors})

    else:
        form = AuthenticationForm()
        return JsonResponse({"status": 0, "case": form.errors})

@csrf_exempt
def logout(request):
    auth_logout(request)
    return JsonResponse({"status": 1})

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return JsonResponse({"status": 1})
        else:
            # form = MyUserCreationForm()
            return JsonResponse({"status": 0, "case": form.errors})
    
    else:
        return JsonResponse({"status": 0})