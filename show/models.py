from django.db import models

# Create your models here.
class First(models.Model):
    id = models.AutoField
    trade = models.CharField(max_length=100,default='')
    subject = models.CharField(max_length=100,default='')
    title = models.CharField(max_length=100,default='')
    any_message = models.CharField(max_length=500,default='',null=True,blank=True)
    File = models.FileField(upload_to='media/first',default='')
    

    def __str__(self):
        return self.trade
    

class Second(models.Model):
    id = models.AutoField
    trade = models.CharField(max_length=100,default='')
    subject = models.CharField(max_length=100,default='')
    title = models.CharField(max_length=100,default='')
    any_message = models.CharField(max_length=500,default='',null=True,blank=True)
    File = models.FileField(upload_to='media/second',default='')
    
    def __str__(self):
        return self.trade

class Third(models.Model):
    id = models.AutoField
    trade = models.CharField(max_length=100,default='')
    subject = models.CharField(max_length=100,default='')
    title = models.CharField(max_length=100,default='')
    any_message = models.CharField(max_length=500,default='',null=True,blank=True)
    File = models.FileField(upload_to='media/third',default='')

    def __str__(self):
        return self.trade

class Fourth(models.Model):
    id = models.AutoField
    trade = models.CharField(max_length=100,default='')
    subject = models.CharField(max_length=100,default='')
    title = models.CharField(max_length=100,default='')
    any_message = models.CharField(max_length=500,default='',null=True,blank=True)
    File = models.FileField(upload_to='media/fourth',default='')

    def __str__(self):
        return self.trade

class Fifth(models.Model):
    id = models.AutoField
    trade = models.CharField(max_length=100,default='')
    subject = models.CharField(max_length=100,default='')
    title = models.CharField(max_length=100,default='')
    any_message = models.CharField(max_length=500,default='',null=True,blank=True)
    File = models.FileField(upload_to='media/fifth',default='')

    def __str__(self):
        return self.trade

class Sixth(models.Model):
    id = models.AutoField
    trade = models.CharField(max_length=100,default='')
    subject = models.CharField(max_length=100,default='')
    title = models.CharField(max_length=100,default='')
    any_message = models.CharField(max_length=500,default='',null=True,blank=True)
    File = models.FileField(upload_to='media/sixth',default='')

    def __str__(self):
        return self.trade


