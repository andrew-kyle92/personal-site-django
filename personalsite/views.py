from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.conf import settings
from django.core.mail import EmailMessage, get_connection, send_mail

import datetime
from dateutil.relativedelta import relativedelta

from .forms import ContactForm


# Create your views here.
def index(request):
    title = "Home | Andrew Kyle's Personal Site"
    template = "index.html"
    dob = datetime.datetime(1992, 1, 29)
    preset_date = datetime.datetime.today()
    it_start = datetime.datetime(2016, 5, 12)
    time_diff_music = relativedelta(preset_date, dob)
    time_diff_it = relativedelta(preset_date, it_start)
    age = time_diff_music.years
    it_exp = time_diff_it.years
    guitar_exp = age - 12
    year = datetime.datetime.now().strftime("%Y")

    context = {
        "it_exp": it_exp,
        "guitar_exp": guitar_exp,
        "year": year,
        "title": title,
        "form": ContactForm(request.POST)
    }

    return render(request, template, context)


def send_message(request):
    email_data = request.POST
    subject = "New message from Personal Site"
    phone_number = email_data["phone_number"]
    sender_name = email_data["name"]
    sender_email = email_data["email"]
    message = email_data["message"] + (f"\n<p>Sender's Name: {sender_name} ({sender_email})</p>"
                                       f"\n<p>Sender's phone number: {phone_number}.<p>")
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER]
    # with get_connection(settings.EMAIL_BACKEND) as conn:
    #     EmailMessage(subject, message, email_from, recipient_list, connection=conn).send()
    send_mail(subject, message, email_from, recipient_list, html_message=message)
    return HttpResponseRedirect('/#contact')
    # return JsonResponse({'email_data': email_data}, safe=False)
