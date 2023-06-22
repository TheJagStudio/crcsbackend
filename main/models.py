from django.db import models


class State(models.Model):
    stateName = models.CharField(max_length=500)
    stateCode = models.CharField(max_length=50)
    isUt = models.BooleanField(default=False)

    def __str__(self):
        return self.stateName

class District(models.Model):
    districtName = models.CharField(max_length=500)
    districtCode = models.CharField(max_length=50,null=True,blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.districtName

class SocietyType(models.Model):
    societyType = models.CharField(max_length=500)
    typeCode = models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.societyType

class Application(models.Model):
    societyName = models.CharField(max_length=500)
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True,blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE,null=True,blank=True)
    societyType = models.ForeignKey(SocietyType, on_delete=models.CASCADE,null=True,blank=True)
    receivedDate = models.DateField(null=True,blank=True)
    disposalDate = models.DateField(null=True,blank=True)

class Society(models.Model):
    societyName = models.CharField(max_length=500)
    Address = models.CharField(max_length=1000,null=True,blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True,blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE,null=True,blank=True)
    Date = models.DateField(null=True,blank=True)
    societyType = models.ForeignKey(SocietyType, on_delete=models.CASCADE,null=True,blank=True)

class Bank(models.Model):
    bankName = models.CharField(max_length=500)
    Address = models.CharField(max_length=1000,null=True,blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True,blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE,null=True,blank=True)

class Liquidation(models.Model):
    societyName = models.CharField(max_length=500)
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True,blank=True)
    nameOfLiquidator = models.CharField(max_length=500,null=True,blank=True)
    appoinmentDate = models.DateField(null=True,blank=True)
    validityDate = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=100,null=True,blank=True)

class User(models.Model):
    name = models.CharField(max_length=500)
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True,blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE,null=True,blank=True)
    societyType = models.ForeignKey(SocietyType, on_delete=models.CASCADE,null=True,blank=True)
    society = models.ForeignKey(Society, on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    panNo = models.CharField(max_length=20,null=True,blank=True)
    tanNo = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=1000,null=True,blank=True)
    designation = models.CharField(max_length=100,null=True,blank=True)
    mobileNo = models.CharField(max_length=20,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    taxNo = models.CharField(max_length=20,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name