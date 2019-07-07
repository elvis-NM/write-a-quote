from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from apps.quotes.models import Quote
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def new(req):
    return render(req, "users/new.html")


def create(req):
    errors = User.objects.validate(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
            return redirect("users:new")
    else:
        user = User.objects.create_user(req.POST)
        req.session["user_id"] = user.id
    return redirect("quotes:index")


def login(req):
    valid, result = User.objects.login(req.POST)
    if not valid:
        messages.error(req, result)
        return redirect("users:new")
    else:
        req.session["user_id"] = result.id
    return redirect("quotes:index")


def logout(req):
    req.session.clear()

    return redirect("users:new")


def edit(req, user_id):
    if "user_id" not in req.session:
        return redirect("users:new")

    try:
        context = {"user": User.objects.get(id=req.session["user_id"])}
        print(req.POST)
    except ObjectDoesNotExist:
        return redirect("quotes:index")

    return render(req, "users/edit.html", context)


def update(req, user_id):
    errors = User.objects.updateerror(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect("users:edit", user_id=user_id)
    User.objects.update(req.POST, user_id)
    return redirect("quotes:index")
