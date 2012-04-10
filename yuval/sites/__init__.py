from sites.models import pageCMS

def cms_processor(request):
    return { 'pages': [{'link':p['paraName'],'header':p['header']}
    for p in pageCMS.get_pages()] ,'locale':request.GET.get('locale','he')}
