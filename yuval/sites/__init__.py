from sites.models import pageCMS

def cms_processor(request):
    locale = request.GET.get('locale')
    if locale:
        request.session['locale'] = locale
    else:
        locale = request.session.get('locale','he')	
    return { 'pages': [{'link':p['paraName'],'header':p['header']}
    for p in pageCMS.get_pages()] ,'locale':locale}
