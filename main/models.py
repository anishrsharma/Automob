from django.db import models

# Create your models here.


class Slots(models.Model):
    type = models.CharField(max_length=50)
    block = models.CharField(max_length=10)
    slots = models.CharField(max_length=10)
    # free = models.CharField(max_length=10)

class ChildSlots(models.Model):
    block = models.CharField(max_length=50)
    slot_no = models.CharField(max_length=10)
    type = models.CharField(max_length=50,default=None)
    free = models.CharField(max_length=10)
    ticket_no = models.CharField(max_length=100, default="")




class Bookings(models.Model):
    type = models.CharField(max_length=50)
    ticket_id = models.CharField(max_length=50)
    vehicle_no = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=50)
    block_id = models.CharField(max_length=10)
    slot_no = models.CharField(max_length=10)
    entry_date_time = models.CharField(max_length=50)
    exit_date_time = models.CharField(max_length=50)
    active = models.CharField(max_length=10, default="")
    price = models.CharField(max_length=10, default="")



class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)






