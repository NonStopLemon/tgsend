from django.urls import path
from . import views

urlpatterns = [
    path('<str:site_name>/<int:error>/<str:url>',
         views.send_message, name='send_message'),
]
# <str:site_name>/<str:error>/
