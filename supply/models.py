from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Account(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=10)

    def __str__(self):
        return self.account_number
