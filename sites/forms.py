__author__ = 'voskov'

from django.forms.models import ModelForm
from sites.models import pageCMS

class PageForm(ModelForm):
    class Meta:
        modle = pageCMS