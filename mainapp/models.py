from django.db import models


class InsuranceType(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title