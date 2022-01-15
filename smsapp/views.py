from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client
from decouple import config


def broadcast_sms(request):
    message_to_broadcast = ("Would you like to play basketball at the Legacy Center tomorrow at 6am? Reply '0' for NO or '1' for YES.")
    
    client = Client(
        settings.TWILIO_ACCOUNT_SID,
        settings.TWILIO_AUTH_TOKEN,
    )
    
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)
            
    return HttpResponse("Messages sent!", 200)


def incoming_sms(request):
    return HttpResponse("Message received!", 200)

