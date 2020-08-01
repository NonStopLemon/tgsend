from django.http import HttpResponse


def l(request):
    return HttpResponse(status=200)
