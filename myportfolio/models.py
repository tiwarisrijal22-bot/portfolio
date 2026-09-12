from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=55)
    phone = models.CharField(max_length=13)
    message = models.TextField()
    contact_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
