# catalog/models.py
from django.db import models      #  ←  missing line

class Product(models.Model):
    sku   = models.CharField(max_length=32, unique=True)
    name  = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.sku})"



class Order(models.Model):
    customer   = models.ForeignKey("customers.CustomerProfile",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return sum(i.subtotal for i in self.items.all())


class OrderItem(models.Model):
    order    = models.ForeignKey(Order, related_name="items",
                                 on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.PROTECT)
    qty      = models.PositiveSmallIntegerField()
    price    = models.DecimalField(max_digits=9, decimal_places=2)

    @property
    def subtotal(self):
        return self.qty * self.price
