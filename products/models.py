from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    supplier = models.CharField(max_length=255)
    purchase_price = models.DecimalField(max_digits=5, decimal_places=2)
    margin = models.DecimalField(max_digits=5, decimal_places=2, editable=False)
    last_modification = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        self.margin = self.price - self.purchase_price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
