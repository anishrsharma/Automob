from django.shortcuts import render
from django.http import HttpResponse

from .models import Slots,ChildSlots,Bookings,User
from django.utils import timezone

import string
import random
import json

import hashlib
import os
import time

from datetime import datetime
# from pytz import timezone

from datetime import datetime, timedelta

# Create your views here.


def generate_unique_id():
    timestamp = int(time.time())
    random_number = random.randint(1000000000, 9999999999)
    data = str(timestamp) + str(random_number)
    hashed_data = hashlib.sha1(data.encode()).hexdigest()
    unique_id = hashed_data[:10]
    return unique_id.upper()



def say_hello(request):
    # return HttpResponse("Hello world...")
    # curr_dt = timezone.now().strftime("%I:%M %p %d-%m-%Y")
    print('----------------------------')
    base_price = 100
    hr = 1

    # Parse the input date string
    input_date_str = 'March 8, 2024, 8:32 p.m.'
    input_format = '%B %d, %Y, %I:%M %p'
    input_datetime = datetime.strptime(input_date_str, input_format)

    # Convert the datetime object to the desired format
    output_format = '%Y-%m-%d %H:%M:%S.%f+00:00'
    output_datetime_str = input_datetime.strftime(output_format)

    print(output_datetime_str)



    print('----------------------------')
    price = base_price*hr
    print(price)
    print('----------------------------')





    return render(request,'hello.html',{'curr_dt':curr_dt})


def parking_list_page(request):
    obj_bookings = Bookings.objects.all().order_by('-id')
    return render(request,'parking_list.html',{'obj_bookings': obj_bookings})


def logout(request):
    responseData = {
        'status': 'ok'
    }
    return HttpResponse(json.dumps(responseData), content_type="application/json")


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj_user = User.objects.filter(username=username, password=password)

        if obj_user:
            responseData = {
                'status': 'ok'
            }
        else:
            responseData = {
                'status': 'error'
            }
        
        return HttpResponse(json.dumps(responseData), content_type="application/json")

    else:
        return render(request,'login.html')


def checkout_page(request):
    
    if request.method == 'POST':
        ticket_id = request.POST.get('ticket_id')

        obj_booking = Bookings.objects.get(ticket_id=ticket_id)
        obj_booking.active = 'No'
        obj_booking.exit_date_time = timezone.now().strftime("%I:%M %p %d-%m-%Y")
        obj_booking.save()

        obj_child_slot = ChildSlots.objects.get(ticket_no=ticket_id)
        obj_child_slot.free = 'Yes'
        obj_child_slot.ticket_no = ""
        obj_child_slot.save()
        
        responseData = {
            'status': 'ok'
        }

        return HttpResponse(json.dumps(responseData), content_type="application/json")

    else:
        return render(request,'checkout.html')






def booking_page(request):

    if request.method == 'POST':

        status = None

        vehicle_no = request.POST.get('vehicle_no')
        slot_type = request.POST.get('slot_type')
        unique_id = generate_unique_id()
        

        obj_empty_slots = ChildSlots.objects.filter(type=slot_type, free='Yes')
        
        if obj_empty_slots:
            # print(obj_empty_slots[0].id)
            slot_id = obj_empty_slots[0].id
            block_id = obj_empty_slots[0].block
            slot_no = obj_empty_slots[0].slot_no
            entry_date_time = timezone.now().strftime("%I:%M %p %d-%m-%Y")


            # occupying the child slot
            obj_child_slot = ChildSlots.objects.get(id=slot_id)
            obj_child_slot.free = 'No'
            obj_child_slot.ticket_no = unique_id
            obj_child_slot.save()


            price = '100'
            if(slot_type == '2-Wheeler'):
                price = '50'


            # Booking the slot
            qry = Bookings(ticket_id=unique_id, vehicle_no=vehicle_no.upper(), vehicle_type=slot_type, block_id=block_id, slot_no=slot_no,entry_date_time=entry_date_time, active="Yes",price=price)  
            qry.save()

            status = "ok"
        
        else:
            status = "Slot is not available"
            print("Slot is not available")

        responseData = {
            'status': status
        }

        return HttpResponse(json.dumps(responseData), content_type="application/json")
        
    else:
        return render(request,'booking.html')




def home_page(request):
    return render(request,'home.html')


def info_page(request,ticket_no):

    obj_booking = Bookings.objects.get(ticket_id=ticket_no)

    return render(request,'info.html',{
        'obj_booking':obj_booking
    })


def status_page(request):

    obj_slots = Slots.objects.all()

    obj_child_slots = ChildSlots.objects.all()
    


    if obj_slots:
        return render(request, 'status.html', {
            'obj_slots': obj_slots,
            'obj_child_slots': obj_child_slots,

        })
    
    return render(request,'status.html')




def slot_page(request):
    if request.method == 'POST':
        block_name = request.POST.get('block_name')
        number_of_slots = request.POST.get('number_of_slots')
        slot_type = request.POST.get('slot_type')

        # print(block_name)
        # print(number_of_slots)
        # print(slot_type)

        obj_slots = Slots.objects.filter(block=block_name)

        block_id = None
        for i in obj_slots:
            block_id = i.id
        
        if(block_id):
            # update the row

            # deleting the previous child slots rows
            ChildSlots.objects.filter(block=block_name).delete()


            obj = Slots.objects.get(id=block_id)

            obj.type = slot_type
            obj.slots = number_of_slots
            obj.save()


            for i in range(1, int(number_of_slots)+1):
                qry2 = ChildSlots(block=block_name, slot_no=i, free='Yes', type=slot_type)
                qry2.save()


            responseData = {
                'status': 'updated'
            }
         

        else:
            # add new row
            qry1 = Slots(type=slot_type, block=block_name, slots=number_of_slots)  
            qry1.save()
            
            for i in range(1, int(number_of_slots)+1):
                qry2 = ChildSlots(block=block_name, slot_no=i, free='Yes',type=slot_type )
                qry2.save()


            responseData = {
                'status': 'added'
            }



        return HttpResponse(json.dumps(responseData), content_type="application/json")
        exit

    else:
        return render(request,'slots.html')




def invoice_page(request,ticket_no):

    obj_booking = Bookings.objects.get(ticket_id=ticket_no)

    return render(request,'invoice.html',{
        'obj_booking':obj_booking
    })

