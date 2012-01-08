from django.core.mail import send_mail
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from contacts.forms import ContactForm
from contacts.models import Contact
import settings

def index(request):
    alphabatized = Contact.objects.all().order_by('name')
    return render_to_response('contacts/index.html', {'alphabatized': alphabatized})


def detail(request, Contact_id):
    c = get_object_or_404(Contact, pk=Contact_id)
    return render_to_response('contacts/detail.html', {'Contact': c})

def add(request):
    if request.method == 'GET':
        form = ContactForm()
        return render_to_response('contacts/New_contact.html',context_instance=RequestContext(request,{'form':form}))
    else:
        cnt = Contact()
        form = ContactForm(request.POST,request.FILES,instance=cnt)
        if form.is_valid():
            form.save()
            send_mail('new contact','there is a new contact', settings.EMAIL_HOST_USER, ['ishai@empeeric.com'])
            return render_to_response('contacts/New_contact.html',context_instance=RequestContext(request,{'form':form,'status':'saved'}))
        else:
            return render_to_response('contacts/New_contact.html',context_instance=RequestContext(request,{'form':form,'status':'error'}))
