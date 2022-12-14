from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.http import Http404, HttpResponseRedirect

from .models import Latest_product, Subscription, About_us, Team, Contact, Feedback
from .serializers import *
from .forms import FeedbackForms


# Create your views here.


def index_page(request):
    products = Latest_product.objects.all()
    sub = Subscription.objects.all()
    about = About_us.objects.all()
    form = FeedbackForms()
    if request.method == "POST":
        form = FeedbackForms(request.POST)
        if form.is_valid():
            name_user = form.cleaned_data.get("name_field")
            email_user = form.cleaned_data.get("email_field")
            phone_user = form.cleaned_data.get("phone_field")
            message_user = form.cleaned_data.get("message_field")
            form.clean()
            Feedback_data = Feedback.objects.create(
                name=name_user, email=email_user, phone=phone_user, message=message_user
            )
        return HttpResponseRedirect("/feedback")
    else:
        form = FeedbackForms()
    return render(
        request,
        "about_app/index.html",
        {"products": products, "subscriptions": sub, "about": about, "form": form},
    )


def about_page(request):
    about = About_us.objects.all()
    team = Team.objects.all()
    form = FeedbackForms()

    if request.method == "POST":
        form = FeedbackForms(request.POST)
        if form.is_valid():
            name_user = form.cleaned_data.get("name_field")
            email_user = form.cleaned_data.get("email_field")
            phone_user = form.cleaned_data.get("phone_field")
            message_user = form.cleaned_data.get("message_field")
            form.clean()

            Feedback_data = Feedback.objects.create(
                name=name_user, email=email_user, phone=phone_user, message=message_user
            )
        return HttpResponseRedirect("/feedback")
    else:
        form = FeedbackForms()

    return render(
        request, "about_app/about.html", {"about": about, "team": team, "form": form}
    )


def contact_page(request):
    contacts = Contact.objects.all()
    form = FeedbackForms()

    if request.method == "POST":
        form = FeedbackForms(request.POST)
        if form.is_valid():
            name_user = form.cleaned_data.get("name_field")
            email_user = form.cleaned_data.get("email_field")
            phone_user = form.cleaned_data.get("phone_field")
            message_user = form.cleaned_data.get("message_field")
            form.clean()

            Feedback_data = Feedback.objects.create(
                name=name_user, email=email_user, phone=phone_user, message=message_user
            )
        return HttpResponseRedirect("/feedback")
    else:
        form = FeedbackForms()

    return render(
        request, "about_app/contact.html", {"contact": contacts, "form": form}
    )


def faq_page(request):
    sub = Subscription.objects.all()
    about = About_us.objects.all()
    form = FeedbackForms()

    if request.method == "POST":
        form = FeedbackForms(request.POST)
        if form.is_valid():
            name_user = form.cleaned_data.get("name_field")
            email_user = form.cleaned_data.get("email_field")
            phone_user = form.cleaned_data.get("phone_field")
            message_user = form.cleaned_data.get("message_field")
            form.clean()

            Feedback_data = Feedback.objects.create(
                name=name_user, email=email_user, phone=phone_user, message=message_user
            )
        return HttpResponseRedirect("/feedback")
    else:
        form = FeedbackForms()

    return render(
        request,
        "about_app/faq.html",
        {"subscriptions": sub, "about": about, "form": form},
    )


def price_page(request):
    sub = Subscription.objects.all()
    form = FeedbackForms()

    if request.method == "POST":
        form = FeedbackForms(request.POST)
        if form.is_valid():
            name_user = form.cleaned_data.get("name_field")
            email_user = form.cleaned_data.get("email_field")
            phone_user = form.cleaned_data.get("phone_field")
            message_user = form.cleaned_data.get("message_field")
            form.clean()

            Feedback_data = Feedback.objects.create(
                name=name_user, email=email_user, phone=phone_user, message=message_user
            )
        return HttpResponseRedirect("/feedback")
    else:
        form = FeedbackForms()

    return render(
        request, "about_app/pricing.html", {"subscriptions": sub, "form": form}
    )


def product_page(request):
    products = Latest_product.objects.all()
    form = FeedbackForms()

    if request.method == "POST":
        form = FeedbackForms(request.POST)
        if form.is_valid():
            name_user = form.cleaned_data.get("name_field")
            email_user = form.cleaned_data.get("email_field")
            phone_user = form.cleaned_data.get("phone_field")
            message_user = form.cleaned_data.get("message_field")
            form.clean()

            Feedback_data = Feedback.objects.create(
                name=name_user, email=email_user, phone=phone_user, message=message_user
            )
        return HttpResponseRedirect("/feedback")
    else:
        form = FeedbackForms()

    return render(
        request, "about_app/products.html", {"products": products, "form": form}
    )


def product_detail(request, pk):
    product = Latest_product.objects.get(pk=pk)
    all_products = Latest_product.objects.all()
    form = FeedbackForms()

    if request.method == "POST":
        form = FeedbackForms(request.POST)
        if form.is_valid():
            name_user = form.cleaned_data.get("name_field")
            email_user = form.cleaned_data.get("email_field")
            phone_user = form.cleaned_data.get("phone_field")
            message_user = form.cleaned_data.get("message_field")
            form.clean()

            Feedback_data = Feedback.objects.create(
                name=name_user, email=email_user, phone=phone_user, message=message_user
            )
        return HttpResponseRedirect("/feedback")
    else:
        form = FeedbackForms()

    return render(
        request,
        "about_app/product_detail.html",
        {"product": product, "products": all_products, "form": form},
    )


def feedback_page(request):
    feedback = Feedback.objects.all()
    form = FeedbackForms(request.POST)

    if request.method == "POST":
        form = FeedbackForms(request.POST)
        if form.is_valid():
            name_user = form.cleaned_data.get("name_field")
            email_user = form.cleaned_data.get("email_field")
            phone_user = form.cleaned_data.get("phone_field")
            message_user = form.cleaned_data.get("message_field")
            form.clean()

            Feedback_data = Feedback.objects.create(
                name=name_user, email=email_user, phone=phone_user, message=message_user
            )
        return HttpResponseRedirect("/feedback")
    else:
        form = FeedbackForms()

    return render(
        request, "about_app/feedback.html", {"feedback": feedback, "form": form}
    )


def subscriptions_detail(request, pk):
    all_sub = Subscription.objects.all()
    sub = Subscription.objects.get(pk=pk)
    form = FeedbackForms(request.POST)

    if request.method == "POST":
        form = FeedbackForms(request.POST)
        if form.is_valid():
            name_user = form.cleaned_data.get("name_field")
            email_user = form.cleaned_data.get("email_field")
            phone_user = form.cleaned_data.get("phone_field")
            message_user = form.cleaned_data.get("message_field")
            form.clean()

            Feedback_data = Feedback.objects.create(
                name=name_user, email=email_user, phone=phone_user, message=message_user
            )
        return HttpResponseRedirect("/feedback")
    else:
        form = FeedbackForms()

    return render(
        request,
        "about_app/subscription_detail.html",
        {"all_sub": all_sub, "sub": sub, "form": form},
    )


def team_detail(request, pk):
    all_team = Team.objects.all()
    team = Team.objects.get(pk=pk)
    form = FeedbackForms()

    if request.method == "POST":
        form = FeedbackForms(request.POST)
        if form.is_valid():
            name_user = form.cleaned_data.get("name_field")
            email_user = form.cleaned_data.get("email_field")
            phone_user = form.cleaned_data.get("phone_field")
            message_user = form.cleaned_data.get("message_field")
            form.clean()

            Feedback_data = Feedback.objects.create(
                name=name_user, email=email_user, phone=phone_user, message=message_user
            )
        return HttpResponseRedirect("/feedback")
    else:
        form = FeedbackForms()

    return render(
        request,
        "about_app/team_detail.html",
        {"all_team": all_team, "team": team, "form": form},
    )


# API viewsets
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Latest_product.objects.all()
    serializer_class = ProductSerializer


class SubViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
