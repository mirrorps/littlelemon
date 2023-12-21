# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu
from django.core import serializers
from .models import Booking
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework import generics, viewsets, status, permissions
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ValidationError
from rest_framework.response import Response


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

@api_view()
@permission_classes([IsAuthenticated])
def book(request):
    form = BookingForm()
    # if request.method == 'POST':
    #     form = BookingForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if exist==False:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('date',datetime.today().date())

    bookings = Booking.objects.all().filter(reservation_date=date)
    print(bookings)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')

# def bookings(request):
#     if request.method == 'POST':
#         data = json.load(request)
#         exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
#             reservation_slot = data['reservation_slot']
#         ).exists()
        
#         if exist == False:
#             booking = Booking(
#                 first_name=data['first_name'],
#                 reservation_date=data['reservation_date'],
#                 reservation_slot=data['reservation_slot']
#             )
#             booking.save()
#         else:
#             return HttpResponse("{'error':1}", content_type = 'application/json')
        
#         date = request.GET.get('date',datetime.today().date())
#         bookings = Booking.objects.all().filter(reservation_date=date)
#         booking_json = serializers.serialize('json', bookings)
        
#         return HttpResponse(booking_json, content_type = 'application/json')

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer_class_custom = BookingSerializer(data=request.POST)
        serializer_class_custom.is_valid(raise_exception=True)
        
        exists = Booking.objects.filter(
            reservation_date=request.POST.get('reservation_date'),
            reservation_slot=request.POST.get('reservation_slot'),
        )
        
        if exists:
            return Response({'message': 'Slot is already taken for the given date'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        booking = Booking()
        booking.first_name = request.POST.get('first_name')
        booking.reservation_date = request.POST.get('reservation_date')
        booking.reservation_slot = request.POST.get('reservation_slot')
        booking.save()
        
        return Response({'message': 'Booking successfully saved'},status=status.HTTP_201_CREATED)
        
        
        
    
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated]