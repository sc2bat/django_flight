from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import  Admins, Books, Airplanes, Airports, Flights, Passports, Users
from .serializers import AdminsSerializer, BooksSerializer, AirplanesSerializer, AirportsSerializer, FlightsSerializer, PassportsSerializer, UsersSerializer
from rest_framework.parsers import JSONParser
from django.db.models import Q

# Create your views here.

@csrf_exempt
def admin_test(request):
    if request.method == 'GET':
        snippets = Admins.objects.all()
        serializer = AdminsSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdminsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def flight_list(request, flight_id):

    obj = Flights.objects.get(flight_id=flight_id)

    if request.method == 'GET':
        serializer = FlightsSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

# @csrf_exempt
# def airport_test(request):

#     if request.method == 'GET':
#         airport_id = request.GET.get('airport_id', None)
#         is_deleted = request.GET.get('is_deleted', None)

#         try:
#             obj = Airports.objects.filter(airport_id=airport_id, is_deleted=is_deleted)
#             serializer = AirportsSerializer(obj)
#             return JsonResponse(serializer.data, safe=False)

#         except Airports.DoesNotExist:
#             return JsonResponse({}, safe=False)

@csrf_exempt
def flight_test(request):

    if request.method == 'GET':
        id = request.GET.get('flight_id')
        isDeleted = request.GET.get('is_deleted')

        query = Q(flight_id=id) & Q(is_deleted=isDeleted)

        try:
            obj = Flights.objects.get(query)
            serializer = FlightsSerializer(obj)
            return JsonResponse(serializer.data, safe=False)

        except Flights.DoesNotExist:
            return JsonResponse({}, safe=False)

# start here!

@csrf_exempt
def admin(request):

    if request.method == 'GET':
        id = request.GET.get('admin_id', None)
        is_deleted = request.GET.get('is_deleted', None)

        try:
            query = {}
            if id is not None:
                query['admin_id'] = id
            if is_deleted is not None:
                query['is_deleted'] = is_deleted

            if query:
                obj = Admins.objects.get(**query)
                serializer = AdminsSerializer(obj)
                return JsonResponse(serializer.data, safe=False)
            else:
                objs = Admins.objects.all()
                serializer = AdminsSerializer(objs, many=True)
                return JsonResponse(serializer.data, safe=False)

        except Admins.DoesNotExist:
            return JsonResponse({}, safe=False)

@csrf_exempt
def passport(request):

    if request.method == 'GET':
        id = request.GET.get('passport_id', None)
        is_deleted = request.GET.get('is_deleted', None)

        try:
            query = {}
            if id is not None:
                query['passport_id'] = id
            if is_deleted is not None:
                query['is_deleted'] = is_deleted

            if query:
                obj = Passports.objects.get(**query)
                serializer = PassportsSerializer(obj)
                return JsonResponse(serializer.data, safe=False)
            else:
                objs = Passports.objects.all()
                serializer = PassportsSerializer(objs, many=True)
                return JsonResponse(serializer.data, safe=False)

        except Passports.DoesNotExist:
            return JsonResponse({}, safe=False)


@csrf_exempt
def flight(request):

    if request.method == 'GET':
        id = request.GET.get('flight_id', None)
        is_deleted = request.GET.get('is_deleted', None)

        try:
            query = {}
            if id is not None:
                query['flight_id'] = id
            if is_deleted is not None:
                query['is_deleted'] = is_deleted

            if query:
                obj = Flights.objects.get(**query)
                serializer = FlightsSerializer(obj)
                return JsonResponse(serializer.data, safe=False)
            else:
                objs = Flights.objects.all()
                serializer = FlightsSerializer(objs, many=True)
                return JsonResponse(serializer.data, safe=False)

        except Flights.DoesNotExist:
            return JsonResponse({}, safe=False)
    

@csrf_exempt
def book(request):

    if request.method == 'GET':
        id = request.GET.get('book_id', None)
        is_deleted = request.GET.get('is_deleted', None)

        try:
            query = {}
            if id is not None:
                query['book_id'] = id
            if is_deleted is not None:
                query['is_deleted'] = is_deleted

            if query:
                obj = Books.objects.get(**query)
                serializer = BooksSerializer(obj)
                return JsonResponse(serializer.data, safe=False)
            else:
                objs = Books.objects.all()
                serializer = BooksSerializer(objs, many=True)
                return JsonResponse(serializer.data, safe=False)

        except Books.DoesNotExist:
            return JsonResponse({}, safe=False)

@csrf_exempt
def airport(request):

    if request.method == 'GET':
        id = request.GET.get('airport_id', None)
        is_deleted = request.GET.get('is_deleted', None)

        try:
            query = {}
            if id is not None:
                query['airport_id'] = id
            if is_deleted is not None:
                query['is_deleted'] = is_deleted

            if query:
                obj = Airports.objects.get(**query)
                serializer = AirportsSerializer(obj)
                return JsonResponse(serializer.data, safe=False)
            else:
                objs = Airports.objects.all()
                serializer = AirportsSerializer(objs, many=True)
                return JsonResponse(serializer.data, safe=False)

        except Airports.DoesNotExist:
            return JsonResponse({}, safe=False)

@csrf_exempt
def user(request):

    if request.method == 'GET':
        id = request.GET.get('user_id', None)
        is_deleted = request.GET.get('is_deleted', None)

        try:
            query = {}
            if id is not None:
                query['user_id'] = id
            if is_deleted is not None:
                query['is_deleted'] = is_deleted

            if query:
                obj = Users.objects.get(**query)
                serializer = UsersSerializer(obj)
                return JsonResponse(serializer.data, safe=False)
            else:
                objs = Users.objects.all()
                serializer = UsersSerializer(objs, many=True)
                return JsonResponse(serializer.data, safe=False)

        except Users.DoesNotExist:
            return JsonResponse({}, safe=False)

@csrf_exempt
def airplane(request):

    if request.method == 'GET':
        id = request.GET.get('airplane_id', None)
        is_deleted = request.GET.get('is_deleted', None)

        try:
            query = {}
            if id is not None:
                query['airplane_id'] = id
            if is_deleted is not None:
                query['is_deleted'] = is_deleted

            if query:
                obj = Airplanes.objects.get(**query)
                serializer = AirplanesSerializer(obj)
                return JsonResponse(serializer.data, safe=False)
            else:
                objs = Airplanes.objects.all()
                serializer = AirplanesSerializer(objs, many=True)
                return JsonResponse(serializer.data, safe=False)

        except Airplanes.DoesNotExist:
            return JsonResponse({}, safe=False)
