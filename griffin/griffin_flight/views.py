from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Admins, Books, Airplanes, Airports, Flights, Passports, Users
from .serializers import AdminsSerializer, BooksSerializer, AirplanesSerializer, AirportsSerializer, FlightsSerializer, PassportsSerializer, UsersSerializer, BooksUpdateSerializer
from rest_framework.parsers import JSONParser
from django.db.models import Q, F
from django.db import connection

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
        admin_name = request.GET.get('admin_name', None)
        email = request.GET.get('email', None)

        try:
            query = {}
            if id is not None:
                query['admin_id'] = id
            if is_deleted is not None:
                query['is_deleted'] = is_deleted
            if email is not None:
                query['email'] = email
            if admin_name is not None:
                query['admin_name'] = admin_name

            if query:
                obj = Admins.objects.filter(**query)
                serializer = AdminsSerializer(obj, many=True)
                return JsonResponse(serializer.data, safe=False)
            else:
                objs = Admins.objects.all()
                serializer = AdminsSerializer(objs, many=True)
                return JsonResponse(serializer.data, safe=False)

        except Admins.DoesNotExist:
            return JsonResponse({}, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdminsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def passport(request):

    if request.method == 'GET':
        id = request.GET.get('passport_id', None)
        is_deleted = request.GET.get('is_deleted', None)
        gender = request.GET.get('gender', None)
        first_name = request.GET.get('first_name', None)
        last_name = request.GET.get('last_name', None)
        email = request.GET.get('email', None)
        phone = request.GET.get('phone', None)
        birthday = request.GET.get('birthday', None)
        book_id = request.GET.get('book_id', None)

        try:
            query = {}
            if id is not None:
                query['passport_id'] = id
            if is_deleted is not None:
                query['is_deleted'] = is_deleted
            if gender is not None:
                query['gender'] = gender
            if first_name is not None:
                query['first_name'] = first_name
            if last_name is not None:
                query['last_name'] = last_name
            if email is not None:
                query['email'] = email
            if phone is not None:
                query['phone'] = phone
            if birthday is not None:
                query['birthday'] = birthday
            if book_id is not None:
                query['book_id'] = book_id

            if query:
                obj = Passports.objects.filter(**query)
                serializer = PassportsSerializer(obj, many=True)
                return JsonResponse(serializer.data, safe=False)
            else:
                objs = Passports.objects.all()
                serializer = PassportsSerializer(objs, many=True)
                return JsonResponse(serializer.data, safe=False)

        except Passports.DoesNotExist:
            return JsonResponse({}, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PassportsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def flight(request):

    if request.method == 'GET':
        id = request.GET.get('flight_id', None)
        is_deleted = request.GET.get('is_deleted', None)
        departure_time = request.GET.get('departure_time', None)
        arrival_time = request.GET.get('arrival_time', None)
        departure_loc = request.GET.get('departure_loc', None)
        arrival_loc = request.GET.get('arrival_loc', None)
        airplane_id = request.GET.get('airplane_id', None)

        try:
            query = {}
            if id is not None:
                query['flight_id'] = id
            if is_deleted is not None:
                query['is_deleted'] = is_deleted
            if departure_time is not None:
                query['departure_time'] = departure_time
            if arrival_time is not None:
                query['arrival_time'] = arrival_time
            if departure_loc is not None:
                query['departure_loc'] = departure_loc
            if arrival_loc is not None:
                query['arrival_loc'] = arrival_loc
            if airplane_id is not None:
                query['airplane_id'] = airplane_id

            if query:
                obj = Flights.objects.filter(**query)
                serializer = FlightsSerializer(obj, many=True)
                return JsonResponse(serializer.data, safe=False)
            else:
                objs = Flights.objects.all()
                serializer = FlightsSerializer(objs, many=True)
                return JsonResponse(serializer.data, safe=False)

        except Flights.DoesNotExist:
            return JsonResponse({}, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FlightsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def book(request):

    if request.method == 'GET':
        id = request.GET.get('book_id', None)
        is_deleted = request.GET.get('is_deleted', None)
        user_id = request.GET.get('user_id', None)
        flight_id = request.GET.get('flight_id', None)
        class_seat = request.GET.get('class_seat', None)
        status = request.GET.get('status', None)
        pay_status = request.GET.get('pay_status', None)
        

        try:
            query = {}
            if id is not None:
                query['book_id'] = id
            if is_deleted is not None:
                query['is_deleted'] = is_deleted
            if user_id is not None:
                query['user_id'] = user_id
            if flight_id is not None:
                query['flight_id'] = flight_id
            if class_seat is not None:
                query['class_seat'] = class_seat
            if status is not None:
                query['status'] = status
            if pay_status is not None:
                query['pay_status'] = pay_status


            if query:
                obj = Books.objects.filter(**query)
                serializer = BooksSerializer(obj, many=True)
                return JsonResponse(serializer.data, safe=False)
            else:
                objs = Books.objects.all()
                serializer = BooksSerializer(objs, many=True)
                return JsonResponse(serializer.data, safe=False)

        except Books.DoesNotExist:
            return JsonResponse({}, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BooksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def airport(request):

    if request.method == 'GET':
        id = request.GET.get('airport_id', None)
        is_deleted = request.GET.get('is_deleted', None)
        airport_code = request.GET.get('airport_code', None)
        airport_name = request.GET.get('airport_name', None)
        latitude = request.GET.get('latitude', None)
        longitude = request.GET.get('longitude', None)
        country = request.GET.get('country', None)

        try:
            query = {}
            if id is not None:
                query['airport_id'] = id
            if is_deleted is not None:
                query['is_deleted'] = is_deleted
            if airport_code is not None:
                query['airport_code'] = airport_code
            if airport_name is not None:
                query['airport_name'] = airport_name
            if latitude is not None:
                query['latitude'] = latitude
            if longitude is not None:
                query['longitude'] = longitude
            if country is not None:
                query['country'] = country

            if query:
                obj = Airports.objects.filter(**query)
                serializer = AirportsSerializer(obj, many=True)
                return JsonResponse(serializer.data, safe=False)
            else:
                objs = Airports.objects.all()
                serializer = AirportsSerializer(objs, many=True)
                return JsonResponse(serializer.data, safe=False)

        except Airports.DoesNotExist:
            return JsonResponse({}, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AirportsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user(request):

    if request.method == 'GET':
        id = request.GET.get('user_id', None)
        is_deleted = request.GET.get('is_deleted', None)
        user_name = request.GET.get('user_name', None)
        email = request.GET.get('email', None)


        try:
            query = {}
            if id is not None:
                query['user_id'] = id
            if is_deleted is not None:
                query['is_deleted'] = is_deleted
            if user_name is not None:
                query['user_name'] = user_name
            if email is not None:
                query['email'] = email

            if query:
                obj = Users.objects.filter(**query)
                serializer = UsersSerializer(obj, many=True)
                return JsonResponse(serializer.data, safe=False)
            else:
                objs = Users.objects.all()
                serializer = UsersSerializer(objs, many=True)
                return JsonResponse(serializer.data, safe=False)

        except Users.DoesNotExist:
            return JsonResponse({}, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

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
                obj = Airplanes.objects.filter(**query)
                serializer = AirplanesSerializer(obj, many=True)
                return JsonResponse(serializer.data, safe=False)
            else:
                objs = Airplanes.objects.all()
                serializer = AirplanesSerializer(objs, many=True)
                return JsonResponse(serializer.data, safe=False)

        except Airplanes.DoesNotExist:
            return JsonResponse({}, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AirplanesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def payment_join(request):
    if request.method == 'GET':
        id = request.GET.get('user_id', None)
        status = request.GET.get('status', None)
        pay_status = request.GET.get('pay_status', None)
        book_id = request.GET.get('book_id', None)

        queryset = Books.objects.select_related('user_id', 'flight_id').prefetch_related('passports').annotate(
                    user_name=F('user_id__user_name'),
                    departure_time=F('flight_id__departure_time'),
                    departure_code=F('flight_id__departure_loc__airport_code'),
                    departure_name=F('flight_id__departure_loc__airport_name'),
                    arrival_code=F('flight_id__arrival_loc__airport_code'),
                    arrival_name=F('flight_id__arrival_loc__airport_name'),
                    first_name=F('passports__first_name'),
                    last_name=F('passports__last_name'),
                ).values(
                    'book_id',
                    'user_id', 
                    'user_name',
                    'flight_id', 
                    'departure_time',
                    'class_seat',
                    'status', 'pay_status', 'pay_amount',
                    'departure_code', 'departure_name',
                    'arrival_code', 'arrival_name',
                    'first_name', 'last_name'
                )

        if pay_status:
            queryset = queryset.filter(pay_status=pay_status)
        else:
            pass
        
        result_set = list(queryset)
        return JsonResponse({'result': result_set})



# book update
@csrf_exempt
def updateBook(request):
    if request.method == 'POST':
        
        jsonData = JSONParser().parse(request)

        print(jsonData)

        try : 
            bookData = Books.objects.get(book_id=jsonData['book_id'])

            if 'class_seat' in jsonData and jsonData['class_seat'] is not None:
                bookData.class_seat = jsonData['class_seat']
            if 'status' in jsonData and jsonData['status'] is not None:
                bookData.status = jsonData['status']
            if 'pay_status' in jsonData and jsonData['pay_status'] is not None:
                bookData.pay_status = jsonData['pay_status']
            if 'pay_amount' in jsonData and jsonData['pay_amount'] is not None:
                bookData.pay_amount = jsonData['pay_amount']
            if 'is_deleted' in jsonData and jsonData['is_deleted'] is not None:
                bookData.is_deleted = jsonData['is_deleted']

            bookData.save()
            
            query = {}
            if jsonData['book_id'] is not None:
                query['book_id'] = bookData.book_id

            if query:
                obj = Books.objects.filter(**query)
                serializer = BooksSerializer(obj, many=True)
                return JsonResponse(serializer.data, safe=False, status=201)
        except ObjectDoesNotExist :
            return JsonResponse({'error' : 'book_id error'}, status = 405)
    else :
        return JsonResponse({'error' : 'method error'}, status = 405)




@csrf_exempt
def get_flights(request):
    if request.method == 'GET':
        try:
            param_from_flight_date = request.GET['from_flight_date']
            param_to_flight_date = request.GET['to_flight_date']
            param_departure_loc = request.GET['departure_loc']
            param_arrival_loc = request.GET['arrival_loc']
        except KeyError as e:
            return JsonResponse({'error': str(e)}, status=400)

        query1 = f"""
            SELECT *
            FROM flights f
            WHERE flight_date = {param_from_flight_date}
            AND departure_loc = {param_departure_loc}
            AND arrival_loc = {param_arrival_loc}
        """
        query2 = f"""
            SELECT *
            FROM flights f
            WHERE flight_date = {param_to_flight_date}
            AND departure_loc = {param_arrival_loc}
            AND arrival_loc = {param_departure_loc}
        """
        
        result1 = Flights.objects.filter(flight_date=param_from_flight_date, 
                                          departure_loc=param_departure_loc,
                                          arrival_loc=param_arrival_loc)
        result2 = Flights.objects.filter(flight_date=param_to_flight_date, 
                                          departure_loc=param_arrival_loc,
                                          arrival_loc=param_departure_loc)

        serializer1 = FlightsSerializer(result1, many=True)
        serializer2 = FlightsSerializer(result2, many=True)

        grouped_results = {
            "from_flight" : serializer1.data,
            "to_flight" : serializer2.data
        }

        return JsonResponse(grouped_results, safe=False)
    else :
        return JsonResponse({'error' : 'method error'}, status = 405)

@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        objs = Users.objects.all()
        serializer = UsersSerializer(objs, many=True)
        return JsonResponse(serializer.data, safe=False)