from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Log

def index(request):
    latest_log_list = Log.objects.order_by("-pub_date")[:5]
    context = {"latest_log_list": latest_log_list}
    return render(request, "logs/index.html", context)

def detail(request, log_id):
    log = get_object_or_404(Log, pk=log_id)
    return render(request, "logs/detail.html", {"log": log})