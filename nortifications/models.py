from django.db import models

class Notif(models.Model):
    types_of_notifications = (
        ("email", "email"),
        ("sms", "sms"),
        ("push", "push")
    )
    type = models.CharField(
        max_length=32,
        choices=types_of_notifications,
        default='email'
    )
    sender = models.CharField(max_length=25)
    receiver = models.CharField(max_length=25)
    msg = models.CharField(max_length=254)

    def __str__(self):
        return self.type + ' ' + self.receiver
