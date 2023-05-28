from django.db import models
from django.urls import reverse


class InsuranceType(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
