__author__ = 'voskov'

from django.forms.models import ModelForm
from contacts.models import Contact

class ContactForm(ModelForm):

    class Meta:
        model = Contact
