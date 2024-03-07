from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

import datetime
from dateutil.relativedelta import relativedelta

from .forms import ContactForm
from .models import send_email


# Create your views here.
def index(request):
    title = "Home | Andrew Kyle's Personal Site"
    template = "personalsite/index.html"
    dob = datetime.datetime(1992, 1, 29)
    preset_date = datetime.datetime.today()
    it_start = datetime.datetime(2016, 5, 12)
    time_diff_music = relativedelta(preset_date, dob)
    time_diff_it = relativedelta(preset_date, it_start)
    age = time_diff_music.years
    it_exp = time_diff_it.years
    guitar_exp = age - 12
    year = datetime.datetime.now().strftime("%Y")

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["hidden_input"] != "":
                redirect("index")
                # re-instantiating the form so that the fields are blank
                form = ContactForm()
            else:
                email_data = {
                    "name": form.cleaned_data["name"],
                    "phone_number": form.cleaned_data["phone_number"],
                    "email": form.cleaned_data["email"],
                    "message": form.cleaned_data["message"],
                }
                send_email(email_data)
                messages.add_message(request, messages.SUCCESS, "Message was successfully sent")
                return redirect(f"/#contact")
    else:
        form = ContactForm()

    context = {
        "it_exp": it_exp,
        "guitar_exp": guitar_exp,
        "year": year,
        "title": title,
        "form": form
    }

    return render(request, template, context)


class EmailView(View):
    @staticmethod
    def get(request, message_data=None):
        title = "Email Template | Andrew Kyle's"
        template = "personalsite/email-template2.html"
        if not message_data:
            message_data = {
                "name": "Andrew Kyle",
                "email": "andrewkyle@andrewkyle.dev",
                "phone_number": "520-243-0047",
                "message": "Test message",
            }
        context = {
            "title": title,
            "message_data": message_data,
        }
        return render(request, template, context)


# def send_message(request):
#     email_data = request.GET
#     decoded_data = dict((k, unquote_plus(v)) for k, v in [item.split('=') for item in email_data.split("&")])
#     subject = "New message from Personal Site"
#     phone_number = decoded_data["phone_number"]
#     sender_name = decoded_data["name"]
#     sender_email = decoded_data["email"]
#     message = decoded_data["message"] + (f"\n<p>Sender's Name: {sender_name} ({sender_email})</p>"
#                                          f"\n<p>Sender's phone number: {phone_number}.<p>")
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [settings.EMAIL_HOST_USER]
#     # with get_connection(settings.EMAIL_BACKEND) as conn:
#     #     EmailMessage(subject, message, email_from, recipient_list, connection=conn).send()
#     send_mail(subject, message, email_from, recipient_list, html_message=message)
#     return redirect('/#contact')
#     # return JsonResponse({'email_data': email_data}, safe=False)
