from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=30)
    people = models.JSONField()
    total_grp_lenngth = models.IntegerField()

    def __str__(self):
        return self.name


class Transaction(models.Model):
    given_by = models.JSONField()
    shares = models.JSONField()
    price = models.IntegerField()

    def __str__(self):
        return f'{self.given_by} - {self.price}'


class Debts(models.Model):
    total_debt = models.JSONField()

    # def __str__(self):
    #     return self.total_debt
