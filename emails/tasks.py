import logging

from celery import shared_task
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


@shared_task
def send_email_to_single_user():
    logger.info("Executing send_email_to_single_user task")
    send_mail(
        "Subject here",
        "Here is the message.",
        "from@example.com",
        ["to@example.com"],
        fail_silently=False,
    )
    return "Task completed"
