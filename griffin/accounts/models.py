from django.db import models

# Create your models here.

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.SmallIntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'users'