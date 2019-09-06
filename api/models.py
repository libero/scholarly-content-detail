from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)


class Journal(models.Model):
    name = models.CharField(max_length=200)
