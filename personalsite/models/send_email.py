# ********** Function for sending an Email **********
from django.conf import settings
from django.core.mail import send_mail


def send_email(email_data):
    subject = "New message from Personal Site"
    phone_number = email_data["phone_number"]
    sender_name = email_data["name"]
    sender_email = email_data["email"]
    message = email_data["message"] + (f"\n<p>Sender's Name: {sender_name} ({sender_email})</p>"
                                       f"\n<p>Sender's phone number: {phone_number}.<p>")
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER, ]
    # with get_connection(settings.EMAIL_BACKEND) as conn:
    #     EmailMessage(subject, message, email_from, recipient_list, connection=conn).send()
    send_mail(subject, message, email_from, recipient_list, html_message=message)
    return True
