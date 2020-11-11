from django.core.exceptions import SuspiciousOperation
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from twilio.request_validator import RequestValidator
from twilio.twiml.voice_response import VoiceResponse
from .settings import twilio_auth_token
import arrow
import logging

logger = logging.getLogger(__name__)


request_validator = RequestValidator(twilio_auth_token)


def validate_django_request(request: HttpRequest):
    try:
        signature = request.META['HTTP_X_TWILIO_SIGNATURE']
    except KeyError:
        is_valid_twilio_request = False
    else:
        is_valid_twilio_request = request_validator.validate(
            signature=signature,
            uri=request.get_raw_uri(),
            params=request.POST,
        )
    if not is_valid_twilio_request:
        # Invalid request from Twilio
        raise SuspiciousOperation()


@require_POST
@csrf_exempt
def welcome(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    if business_hours == 1:
        vr.say("Thank you for calling. Redirecting your call to a human.")
        vr.dial(number='+358402203810')
    else:
        vr.say("We are currently closed.", voice='alice')
        vr.pause(length=0.5)
        vr.say(f"Our business hours are ten till sixteen, Monday though Friday.")
        vr.pause(length=0.5)
        vr.hangup()
    return HttpResponse(str(vr), content_type='text/xml')



def business_hours():
    current_time = int(arrow.now(tz='Europe/Helsinki').format('HH'))
    #current_time_test = int('10')
    logger.debug(type(current_time))
    logger.info(current_time)
    if current_time >= 10 and current_time < 16:
        return 1
    else:
        return 0
    #if current_time > 10 and current_time < 16:
    #    return 0
    #else:
    #    return 1
