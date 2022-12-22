from django.db import models

class Account(models.Model):
    email = models.TextField(default=None, null=True, blank=True) # email for register on site
    password = models.TextField(default=None) # password for registration

    def __str__(self):
        return self.email
