from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import MyView,IPWare

app_name = 'polls'
urlpatterns = [
    path('direct_access/',MyView.as_view()),
    path('ip_access/',IPWare.as_view()),
    # path('getip/',SampleTemplateView.as_view()),
    path('',views.index,name='index'),
]



