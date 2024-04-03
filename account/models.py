from django.db import models
from supplier.models import Supplier

class Account(models.Model):
    account_number = models.CharField(max_length=10)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)