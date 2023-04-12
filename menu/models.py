from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=100, blank=False)
    parent_id = models.IntegerField(null=True)
