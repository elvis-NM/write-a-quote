from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .models import User
from .models import Quote
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def index(req):
    if "user_id" not in req.session:
        return redirect("users:new")
    else:
        context = {
            "user": User.objects.get(id=req.session["user_id"]),
            "quotes": Quote.objects.order_by("-created_at"),
        }
        return render(req, "quotes/quotes.html", context)


def create(req):
    errors = Quote.objects.validate(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect("quotes:index")
    else:
        Quote.objects.create_quote(req.POST, req.session["user_id"])
        print(req.POST)
    return redirect("quotes:index")


def view(req):

    if "user_id" not in req.session:

        return redirect("users:new")

    else:
        user = User.objects.get(id=req.session["user_id"])
        context = {"user": user, "quotes": Quote.objects.all()}
    return render(req, "quotes/view.html", context)


def edit(req, quote_id):
    if "user_id" not in req.session:
        return redirect("users:new")

    try:
        context = {
            "user": User.objects.get(id=req.session["user_id"]),
            "quote": Quote.objects.get(id=quote_id),
        }
        print(req.POST)
    except ObjectDoesNotExist:
        return redirect("quotes:index")

    return render(req, "quotes/edit.html", context)


def update(req, quote_id):
    errors = Quote.objects.validate(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect("quotes:edit", quote_id=quote_id)
    Quote.objects.update(req.POST, quote_id)
    return redirect("quotes:index")


def delete(req, quote_id):
    try:
        quote = Quote.objects.get(id=quote_id)
        quote.delete()
    except ObjectDoesNotExist:
        print("TRIED TO DELETE Quote #{}, DOES NOT EXIST".format(quote_id))

    return redirect("quotes:index")


def like(req, quote_id):
    Quote.objects.add_like(req.session["user_id"], quote_id)
    return redirect("quotes:index")


def unlike(req, quote_id):
    Quote.objects.remove_like(req.session["user_id"], quote_id)
    return redirect("quotes:index")
