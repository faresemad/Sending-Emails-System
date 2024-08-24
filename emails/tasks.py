from celery import shared_task, chord
from django.core.mail import send_mail
from django.contrib.auth.models import User
import logging, datetime

logger = logging.getLogger(__name__)


@shared_task
def send_email_batch(user_ids):
    users = User.objects.filter(id__in=user_ids)
    for user in users:
        subject = "Hello, {}".format(user.username)
        message = "Dear {},\n\nThis is a personalized message just for you!".format(user.username)
        send_mail(subject, message, 'from@example.com', [user.email])
        logger.info("Sent email to {}".format(user.username))


@shared_task
def on_chord_complete(results):
    print("All emails have been sent.")


@shared_task
def send_personalized_emails():
    start_time  = datetime.datetime.now()
    logger.info("Sending personalized emails to all users")
    batch_size = 100  # Adjust batch size as needed
    user_ids = User.objects.values_list('id', flat=True)[:1000]

    batches = [user_ids[i:i + batch_size] for i in range(0, len(user_ids), batch_size)]

    # Create a chord to execute batches in parallel and call the callback when done
    header = [send_email_batch.s(batch) for batch in batches]
    callback = on_chord_complete.s()
    chord(header)(callback)
    end_time  = datetime.datetime.now()
    logger.info("Sent personalized emails to all users in {}".format(end_time - start_time))