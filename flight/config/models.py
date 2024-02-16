from django.db import models

class Admins(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.SmallIntegerField(default=0)

    class Meta:
        app_label = 'flight'
    
class Airplanes(models.Model):
    airplane_id = models.AutoField(primary_key=True)
    first_class_seat = models.IntegerField(default=6)
    business_class_seat = models.IntegerField(default=12)
    economy_class_seat = models.IntegerField(default=60)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.SmallIntegerField(default=0)

class Airports(models.Model):
    airport_id = models.AutoField(primary_key=True)
    airport_code = models.CharField(max_length=100)
    airport_name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.SmallIntegerField(default=0)

class Flights(models.Model):
    flight_id = models.AutoField(primary_key=True)
    departure_time = models.CharField(max_length=100)
    arrival_time = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.SmallIntegerField(default=0)
    departure_loc = models.ForeignKey(Airports)
    arrival_loc = models.ForeignKey(Airports)
    airplane_id = models.ForeignKey(Airplanes)

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.SmallIntegerField(default=0)

class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users)
    flight_id = models.ForeignKey(Flights)
    class_ = models.CharField(max_length=100)
    status = models.IntegerField()
    pay_status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.SmallIntegerField(default=0)

class Passports(models.Model):
    passport_id = models.AutoField(primary_key=True)
    gender = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    birthday = models.CharField(max_length=100)
    book_id = models.ForeignKey(Books)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.SmallIntegerField(default=0)
