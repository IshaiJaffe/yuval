from django.template.context import RequestContext
from sites.forms import PageForm
from sites.models import pageCMS, GalleryImage
from django.shortcuts import render_to_response, get_object_or_404
from django.http import *


def index(request):
    page = pageCMS.get_page('consultation')
    return render_to_response('pages/page.html',context_instance=RequestContext(request,{'page':page,'page_link':page.paraName}))

def gallery(request):
    images = GalleryImage.get_images()# .objects.filter(use=True).order_by('ordinal')
    return render_to_response('pages/gallery.html', context_instance=RequestContext(request,
            {
         #   'latest_article': latest_article,
             'images':images,
             'page_link':'gallery'
        }))
def me(request):
    return render_to_response('pages/me.html', context_instance=RequestContext(request,
            {'page_link':'me'}))

def page(request,page_name):
    page = pageCMS.get_page(page_name)
    return render_to_response('pages/page.html',context_instance=RequestContext(request,{'page':page,'page_link':page.paraName}))

def detail(request, pageCMS_id):
    p = get_object_or_404(pageCMS, pk=pageCMS_id)
    return render_to_response('pages/detail.html', {'pageCMS': p})

def add(request):
    if request.method == 'GET':
        article = pageCMS()
        form = PageForm(request.GET, request.FILES, instance=article)
        return render_to_response('pages/New_article.html', context_instance=RequestContext(request,{'form':form }))
    else:
        art = pageCMS()
        form = PageForm(request.POST, request.FILES, instance=art)
        form.save()
        return render_to_response('sites/index.html', context_instance=RequestContext(request,{'form':form}))
