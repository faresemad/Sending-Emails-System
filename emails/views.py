from django.core.mail import send_mail
from django.http import HttpResponse


def send_mail_view(request):
    send_mail(
        "Subject here",
        "Here is the message.",
        "from@example.com",
        ["to@example.com"],
        fail_silently=False,
    )
    return HttpResponse("Email sent")
