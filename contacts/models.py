from django.db import models


class ContactDetail(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField();
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Getquotes(models.Model):
    city_depature = models.CharField(max_length=200)
    city_deliver = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    dimensions = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15)
    message = models.TextField();
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

