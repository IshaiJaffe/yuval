from django.db import models

def get_last_ordinal_page():
    pages = pageCMS.objects.all().order_by('-ordinal')
    if len(pages):
        return pages[0].ordinal + 1
    else:
        return 0.0

cached_pages = None
cached_pages_dict = {}
cached_images = None

def clear_cache():
    global cached_pages, cached_pages_dict, cached_images
    cached_pages = None
    cached_pages_dict = {}
    cached_images = None

class pageCMS(models.Model):
    paraName = models.CharField('name', max_length=100)
    header = models.CharField('Header', max_length=100)
    subHeader = models.CharField('Sub Header', max_length=1000)
    para = models.TextField('paragraph',max_length=4000)
    pub_date = models.DateTimeField('date published')
    photo = models.FileField('photo', upload_to='photos')
    use = models.BooleanField(default=True)
    ordinal = models.FloatField(default=get_last_ordinal_page)

    def save(self, *args,**kwargs):
        clear_cache()
        super(pageCMS,self).save(*args,**kwargs)

    def __unicode__(self):
        return self.paraName

    @staticmethod
    def get_pages():
        global cached_pages
        if not cached_pages:
            cached_pages = pageCMS.objects.filter(use=True).order_by('ordinal').values('paraName','header')
        return cached_pages
    
    @staticmethod
    def get_page(name):
        global cached_pages_dict
        if name not in cached_pages_dict:
            cached_pages_dict[name] = pageCMS.objects.get(paraName=name)
        return cached_pages_dict[name]

def get_last_ordinal():
    images = GalleryImage.objects.all().order_by('-ordinal')
    if len(images):
        return images[0].ordinal + 1
    else:
        return 0.0

class GalleryImage(models.Model):
    image = models.ImageField('photo',upload_to='photos')
    title = models.TextField(default='')
    use = models.BooleanField(default=True)
    ordinal = models.FloatField(default=get_last_ordinal)

    def save(self, *args,**kwargs):
        clear_cache()
        super(GalleryImage,self).save(*args,**kwargs)

    @staticmethod
    def get_images():
        global cached_images
        if not cached_images:
            cached_images = GalleryImage.objects.filter(use=True).order_by('ordinal')
        return cached_images