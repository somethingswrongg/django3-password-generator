from django.db import models

class Passwords(models.Model):
    name = models.CharField(max_length=14)
    password = models.CharField(max_length=14)
    created_at = models.DateTimeField(auto_now_add = True)