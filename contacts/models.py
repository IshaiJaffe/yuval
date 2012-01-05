from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15) #the '0' of the phone isn't included
    email = models.EmailField(max_length=50)

    def __unicode__(self):
        return self.name