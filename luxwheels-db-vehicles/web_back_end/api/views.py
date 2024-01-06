from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import User, Reservation
from .serializers import UserSerializer, ReservationSerializer

import json
from django.db import IntegrityError


@api_view(['GET'])
def getVehicle(request):
    with open('./vehicle-json/1st.json', 'r') as f:
        vehicle = json.loads(f.read())
        f.closed
    return Response(vehicle)


@api_view(['GET', 'POST'])
def getCreateUser(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        first_name = data["fName"]
        last_name = data["lName"]
        email = data["email"]
        username = data["username"]
        password = data["password"]

        try:
            # password is transparent in the api
            new_user = User(
                first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            new_user.save()
            Token.objects.create(user=new_user)
            return Response(data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def getPostReservation(request):
    if request.method == 'GET':
        meetings = Reservation.objects.all()
        serializer = ReservationSerializer(meetings, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        vehicle_name = data["vehicleName"]
        name = data["fName"] + ' ' + data["lName"]
        email = data["email"]
        contact_number = int(data["contactNumber"])
        payment_method = data["paymentMethod"]

        insurance = ""
        for plan in data["insurancePlan"]["insurance"]:
            insurance += plan + " "

        warranty = data["warranty"]
        service_maintenance = data["serviceMaintenance"]
        comment = data["comment"]
        received_email = bool(data["receivedEmail"])

        new_meeting = Reservation(vehicle_name=vehicle_name, name=name, email=email, contact_number=contact_number, payment_method=payment_method,
                                  insurance_plan=insurance, warranty=warranty, service_maintenance=service_maintenance, comment=comment, received_email=received_email)
        new_meeting.save()
        return Response(data, status=status.HTTP_201_CREATED)

# comment: ""
# contactNumber: "09214779057"
# email: "villanueva@gmail.com"
# fName: "Eunice"
# insurancePlan:
# insurance: (3) ['Service Plan', 'GAP Insurance', 'Tyre and Alloy Insurance']
# [[Prototype]]: Object
# lName: "Villanueva"
# paymentMethod: "installment"
# receivedEmail: "true"
# serviceMaintenance: "premium"
# vehicleName: "AUDI Avant quattro S-Line"
# warranty: "basic"

# STOP HERE:
# 1. check the value first of the get data including the data type
# 2. try to post
# 3.
