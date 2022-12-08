#!/usr/bin/python3

# imports from Django
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from random import random


# This view will return "Welcome to the Phoenix Cafe!" as text
def welcome(request):
    return HttpResponse("Welcome to the Phoenix Cafe!")
def sleepy(request):
    return HttpResponse("Z-z-z-z-z-z!")
def rand(request):
    random_num = random()
    return HttpResponse(random_num)
def greetings(request):
    timenow = datetime.now()
    time = timenow.strftime('%H')
    if time < "12":
        return HttpResponse("Good Morning")
    if time >= "12" and time < "20":
        return HttpResponse("Good Afternoon")
    if time > "20":
        return HttpResponse("Good Night")
