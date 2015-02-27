from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from django.shortcuts import render

from insps.models import Inspection, Description

def index(request):
    latest_insps = Inspection.objects.all().order_by('-date')[:500]

    template = loader.get_template('insps/index.html')
    context = {'latest_insps': latest_insps}
    return render(request, 'insps/index.html', context)

def estab(request, estab_id):
    try:
        estab = Inspection.objects.all().filter(estab_id=estab_id).order_by('date')
    except Inspection.DoesNotExist:
        raise Http404
    return render(request, 'insps/estab.html', { 'estab': estab })


def inspection(request, inspection_key):
    try:
        insp_details = Description.objects.all().filter(inspection_key=inspection_key)
    except Description.DoesNotExist:
        raise Http404
    return render(request, 'insps/inspection.html', { 'insp_details': insp_details })