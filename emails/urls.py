from django.urls import path

from emails.views import send_mail_view

urlpatterns = [
    path("send_mail/", send_mail_view),
]
