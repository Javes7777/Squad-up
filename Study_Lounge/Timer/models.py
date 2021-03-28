from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Timer(models.Model):
    name = models.CharField(max_length = 200)
    when = models.DateTimeField()
    now = timezone.now()

    def __str__(self):
        return str(self.name)

    def  get_absolute_url(self):
        return reverse('Timer:Timer-detail', kwargs={'pk': self.pk } )

