from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError

from booking.models import ReserveTicket, Departure
from booking.forms import ReserveTicketForm


def home(request):
    return render(request, "booking/index.html")


def userTicketView(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ReserveTicketForm(request.POST)
            if form.is_valid():
                reservation = form.save(commit=False)
                departure = Departure.objects.get(pk=reservation.date.pk)
                print(f"Departure ========== {departure}")
                if departure.capacity > 0:
                    reservation.user = request.user
                    reservation.save()

                    # Update the capacity
                    departure.capacity -= 1
                    departure.save()
                    return redirect("booking:home")
                else:
                    form.add_error(None, ValidationError(f"No capacity left for {departure.train.title} on {departure.date}"))
                    return redirect("booking:reserve")
            else:
                return redirect("booking:reserve")
        else:
            form = ReserveTicketForm()
            return render(request, "booking/reserve.html", {'form': form})
    else:
        return redirect("user:login")
