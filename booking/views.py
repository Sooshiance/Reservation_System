from django.shortcuts import render, redirect

from booking.models import ReserveTicket
from booking.forms import ReserveTicketForm


def home(request):
    return render(request, "booking/index.html")


def userTicketView(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ReserveTicketForm(request.POST)
            if form.is_valid():
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.save()
                return redirect("booking:home")
            else:
                return redirect("booking:reserve")
        else:
            form = ReserveTicketForm()
        return render(request, "booking/reserve.html", {'form':form})
    else:
        return redirect("user:login")
