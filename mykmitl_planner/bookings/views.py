from django.shortcuts import render, redirect
from django.views import View
from .models import *

# Event
class EventListPage(View):
    
    def get(self, request):
        return render(request, "event/event-list.html",{

        })
    
class EventDetailPage(View):
    
    def get(self, request):
        return render(request, "event/event-detail.html",{

        })
    
class CreateEventPage(View):
    
    def get(self, request):
        return render(request, "event/staff/create-event.html",{

        })

class EditEventPage(View):
    
    def get(self, request):
        return render(request, "event/staff/edit-event.html",{

        })
    

# Booking
class BookingListPage(View):
    def get(self, request):
        facility = Facility.objects.filter(booking_status='available').values('location').distinct()

        return render(request, "booking/book-list.html",{
            'locations' : facility 
        })
    
class BookFirstPage(View):
    
    def get(self, request, location):
        facilities = Facility.objects.filter(location=location)
        return render(request, "booking/book-first.html",{
            'facility' : facilities
        })

class BookSecondPage(View):
    
    def get(self, request, id):
        facilities = Facility.objects.get(id=id)
        return render(request, "booking/book-second.html",{
            'facilities' : facilities
        })

class CheckAvailableTimes(View):

    def get(self, request, facility_id):

        return
    
    
class BookThirdPage(View):
    
    def get(self, request):
        return render(request, "booking/book-third.html",{

        })
    
class UpcomingBookPage(View):
    
    def get(self, request):
        return render(request, "booking/upcoming.html",{

        })

class PastBookPage(View):
    
    def get(self, request):
        return render(request, "booking/past-book.html",{

        })
    
class BookDetailPage(View):
    
    def get(self, request):
        return render(request, "booking/book-detail.html",{

        })
    
class StaffBookPage(View):
    
    def get(self, request):
        return render(request, "booking/staff/book-staff.html",{

        })
    
class FacilitiesPage(View):
    
    def get(self, request):
        return render(request, "facilities/facilities.html",{

        })