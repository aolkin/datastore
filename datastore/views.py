
from config import config
from config.models import Config

from django.http import HttpResponse

def store(request):
    for i in request.GET.keys():
        config[i] = request.GET[i]
    return HttpResponse("{}: {}".format(i, config[i]))

def get(request):
    out = "<ul>"
    if request.GET:
        for i in request.GET.keys():
            out += "<li>{}: {}</li>".format(i, config[i])
    else:
        for i in Config.objects.all():
            out += "<li>{}: {} ({})</li>".format(i.key, i.value, i.date_modified)
    out += "</ul>"
    return HttpResponse(out)
