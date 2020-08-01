from django.shortcuts import render
from django.http import HttpResponse
from .bot import Bot


def send_message(request, site_name, error, url):
    run = Bot(site_name=site_name, error=error, url=url)

    run.create_message()

    run.sends()

    del run

    return HttpResponse(status=200)
