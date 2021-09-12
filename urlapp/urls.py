
from django.urls import path
from urlapp.views import createUrl,routeLinkUrl


urlpatterns = [
    path('', createUrl),
    path('<slug:id>',routeLinkUrl ),
]
