from django.urls import path

from emails.views import send_emails_to_all_users

urlpatterns = [
    path("send_mail/", send_emails_to_all_users),
]
