from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError

from booking.models import ReserveTicket, Departure
from booking.forms import ReserveTicketForm


def home(request):
    return render(request, "booking/index.html")


def userReserveTicketView(request):
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


def userDeleteTicketView(request, pk):
    if request.user.is_authenticated:
        user = request.user
        if request.method == "POST":
            ticket = ReserveTicket.objects.get(pk=pk,user=user)
            try:
                ticket.delete()
                return redirect("user:profile")
            except:
                raise ValueError("Object does not exist!")
        ticket = get_object_or_404(ReserveTicket, pk=pk)
        return render(request, "booking/delete_ticket.html", {'ticket':ticket})
    else:
        return redirect("user:login")
