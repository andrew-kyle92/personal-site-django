from django.db import models


# Create your models here.
class EmailMessages(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField(max_length=100)
    sender_phone_number = models.CharField(max_length=100)
    sender_message = models.TextField()
