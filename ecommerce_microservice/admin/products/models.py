from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    discount = models.BooleanField(default=False)
    image = models.CharField(max_length=200)
    rating = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    num_sold = models.IntegerField(default=0, blank=True)
    quantity_available = models.PositiveIntegerField(default=100)

    def __str__(self):
        return f"Product: {self.name} id:[{self.product_id}]"
