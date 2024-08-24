import logging

from django.http import HttpResponse

from emails.tasks import send_email_to_single_user

logger = logging.getLogger(__name__)


def send_mail_view(request):
    logger.info("Executing send_mail_view")
    send_email_to_single_user.delay()
    return HttpResponse("Email sent successfully")
