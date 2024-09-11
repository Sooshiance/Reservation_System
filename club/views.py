from django.shortcuts import render, redirect, get_object_or_404

from club.models import FAQ, Rating
from club.forms import RatingForm
from booking.models import Ticket


def seeQuestion(request):
    q = FAQ.objects.all()
    return render(request, "club/faq.html",{'questions':q})


def allTrain(request):
    t = Ticket.objects.all()
    return render(request, "club/allTrain.html", {"trains":t})


def sendComment(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            t = get_object_or_404(Ticket, pk=pk)
            form = RatingForm(request.POST)
            if form.is_valid():
                txt = form.cleaned_data["txt"]
                vote = form.cleaned_data["vote"]
                Rating.objects.create(txt=txt,vote=vote,user=request.user,ticket=t).save()
                return redirect("booking:home")
            else:
                return redirect("club:rating")
        else:
            form = RatingForm()
            return render(request, "club/rating.html", {"form":form})
    else:
        return redirect("user:login")
