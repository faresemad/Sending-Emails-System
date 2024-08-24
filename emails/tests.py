from django.test import TestCase, override_settings
from django.contrib.auth.models import User
from django.core import mail
from .tasks import send_personalized_emails
import logging, datetime

logger = logging.getLogger(__name__)


class EmailSendingTest(TestCase):

    def setUp(self):
        # Create 1000 test users
        logger.info("Creating 1000 test users")
        start_time  = datetime.datetime.now()
        users = [
            User(username=f'user{i}', email=f'user{i}@example.com', password='password')
            for i in range(1000)
        ]
        User.objects.bulk_create(users)
        end_time  = datetime.datetime.now()
        logger.info("Created 1000 test users in {}".format(end_time - start_time))

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_send_emails_to_1000_users(self):
        # Run the Celery task
        send_personalized_emails.apply()

        # Check that 1000 emails were sent
        self.assertEqual(len(mail.outbox), 1000)

        # Optionally, check the content of the first email
        first_email = mail.outbox[0]
        self.assertIn('Hello, user0', first_email.subject)
        self.assertIn('Dear user0', first_email.body)

