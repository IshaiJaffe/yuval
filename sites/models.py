from django.db import models

class pageCMS(models.Model):
    paraName = models.CharField('name', max_length=100)
    header = models.CharField('Header', max_length=100)
    subHeader = models.CharField('Sub Header', max_length=1000)
    para = models.TextField('paragraph')
    pub_date = models.DateTimeField('date published')
    photo = models.ImageField('photo', upload_to='photos')

    def __unicode__(self):
        return self.paraName