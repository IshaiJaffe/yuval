from django.template.context import RequestContext
from sites.forms import PageForm
from sites.models import pageCMS
from django.shortcuts import render_to_response, get_object_or_404
from django.http import *


def index(request):
    latest_article = pageCMS.objects.all().order_by('-pub_date')[:5]
    return render_to_response('pages/index.html', {'latest_article': latest_article})


def detail(request, pageCMS_id):
    p = get_object_or_404(pageCMS, pk=pageCMS_id)
    return render_to_response('pages/detail.html', {'pageCMS': p})

def add(request):
    if request.method == 'GET':
        article = pageCMS()
        return render_to_response('pages/New_article.html', context_instance=RequestContext(request,{'form':form})))
    else:
        art = pageCMS()
        form = PageForm(request.POST, request.FILES, instance)
        form.save()
        return render_to_response('sites/index.html', )
