from website.models import Publication

def showInfos(request):
    return {'mv_pubs' : Publication.objects.order_by('view_number')[:5],
        'mr_pubs' : Publication.objects.order_by('date')[:5],
    }
    