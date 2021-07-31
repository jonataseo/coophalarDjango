from django.db import models


class Client(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return "%s" % self.full_name


class Address(models.Model):
    street_name = models.CharField(max_length=200)
    house_number = models.CharField(max_length=5)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.street_name, self.client)

