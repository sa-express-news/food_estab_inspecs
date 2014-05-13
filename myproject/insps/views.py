from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from django.shortcuts import render

from insps.models import Inspection, Description

def index(request):
    latest_insps = Inspection.objects.filter(date__range=["2013-11-30", "2013-12-31"])
    template = loader.get_template('insps/index.html')
    context = {'latest_insps': latest_insps}
    return render(request, 'insps/index.html', context)

def estab(request, estab_id):
    try:
        estab = Inspection.objects.all().filter(estab_id=estab_id).order_by('-date')
    except Inspection.DoesNotExist:
        raise Http404
    return render(request, 'insps/estab.html', { 'estab': estab })


def inspection(request, inspection_key):
    return HttpResponse("These are the details for this date's inspection of this restaurant %s" % inspection_key)