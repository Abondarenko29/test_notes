from django.db import models


# Create your models here.
class Note(models.Model):

    ROLE_CHOICES = [
        ("pass", "Password"),
        ("imp_info", "Important information"),
        ("info", "Information"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    role = models.CharField(max_length=30,
                            choices=ROLE_CHOICES,
                            default="Information")

    def __str__(self):
        return self.title
