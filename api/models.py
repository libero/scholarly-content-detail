from django.db import models


class Journals(models.Model):
    name = models.CharField(max_length=200)


class Categories(models.Model):
    name = models.CharField(max_length=200)
