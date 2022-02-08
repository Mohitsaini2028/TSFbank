from django.db import models

class addcustomer(models.Model):
    regid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    mobile=models.IntegerField(default=0)
    email=models.EmailField(max_length=254)
    account=models.CharField(max_length=10)
    balance=models.IntegerField(default=0)
    role=models.CharField(max_length=10)
    dt=models.CharField(max_length=1000)

    def __str__(self):
        return self.name + " " + str(self.balance)

class trans(models.Model):
    regid=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=30)
    sacc=models.CharField(max_length=60)
    sb=models.CharField(max_length=15)
    rname=models.CharField(max_length=30)
    amount=models.IntegerField(default=0)
    dt=models.CharField(max_length=1000)

    def __str__(self):
        return self.sname + " " + self.rname
