from django.db import models

# Create your models here.
class Data(models.Model):
    id = models.AutoField
    trade = models.CharField(max_length=100,default='')
    sem = models.IntegerField()
    subject = models.CharField(max_length=100,default='')
    title = models.CharField(max_length=100,default='')
    any_message = models.CharField(max_length=500,default='',null=True,blank=True)
    File = models.FileField(upload_to='media/sixth',default='')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.trade+" - "+str(self.sem)+" - "+self.subject+" - "+self.title
    

class Contact(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name+' - '+self.email +' - ' +self.message
