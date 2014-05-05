from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the restaurant inspections index.")

def detail(request, estab_id):
    return HttpResponse("Detail page for restaurant of estab_id: %s." % estab_id)