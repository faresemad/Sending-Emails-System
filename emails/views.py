import logging

from django.http import HttpResponse

from emails.tasks import send_personalized_emails

logger = logging.getLogger(__name__)


def send_emails_to_all_users(request):
    send_personalized_emails.delay()
    return HttpResponse("Emails are being sent in the background.")
