# ********** Function for sending an Email **********
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email(email_data):
    subject = "New message from Personal Site"
    # phone_number = email_data["phone_number"]
    # sender_name = email_data["name"]
    # sender_email = email_data["email"]
    # message = email_data["message"] + (f"\n<p>Sender's Name: {sender_name} ({sender_email})</p>"
    #                                    f"\n<p>Sender's phone number: {phone_number}.<p>")
    html_message = render_to_string('personalsite/email-template2.html', context={'message_data': email_data})
    plain_message = strip_tags(html_message)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER, ]
    # with get_connection(settings.EMAIL_BACKEND) as conn:
    #     EmailMessage(subject, message, email_from, recipient_list, connection=conn).send()
    send_mail(subject, plain_message, email_from, recipient_list, html_message=html_message)
    return True
