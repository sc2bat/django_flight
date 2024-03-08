from django.db import models

# Create your models here.

class Admins(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.SmallIntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'admins'
    
class Airplanes(models.Model):
    airplane_id = models.AutoField(primary_key=True)
    first_class_seat = models.IntegerField(default=6)
    business_class_seat = models.IntegerField(default=12)
    economy_class_seat = models.IntegerField(default=60)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.SmallIntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'airplanes'

class Airports(models.Model):
    airport_id = models.AutoField(primary_key=True)
    airport_code = models.CharField(max_length=100)
    airport_name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.SmallIntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'airports'

class Flights(models.Model):
    flight_id = models.AutoField(primary_key=True)
    flight_date = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)
    arrival_time = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.SmallIntegerField(default=0)
    departure_loc = models.ForeignKey(Airports, on_delete=models.RESTRICT, related_name='departures', db_column='departure_loc')
    arrival_loc = models.ForeignKey(Airports, on_delete=models.RESTRICT, related_name='arrivals', db_column='arrival_loc')
    airplane_id = models.ForeignKey(Airplanes, on_delete=models.RESTRICT, db_column='airplane_id')

    class Meta:
        managed = False
        db_table = 'flights'

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.SmallIntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'users'

class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.RESTRICT, db_column='user_id')
    flight_id = models.ForeignKey(Flights, on_delete=models.RESTRICT, db_column='flight_id')
    class_seat = models.CharField(max_length=100)
    status = models.IntegerField()
    pay_status = models.IntegerField()
    pay_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.SmallIntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'books'

class Passports(models.Model):
    passport_id = models.AutoField(primary_key=True)
    gender = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    birthday = models.CharField(max_length=100)
    book_id = models.OneToOneField(Books, on_delete=models.RESTRICT, db_column='book_id')
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.SmallIntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'passports'
