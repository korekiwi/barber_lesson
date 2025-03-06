from django.shortcuts import render
from django.views.generic import View, TemplateView

from core.models import Master, Service, Visit
from core.forms import VisitForm

MENU = [
    {'title': 'Главная', 'url': '/', 'active': True},
    {'title': 'Мастера', 'url': '#masters', 'active': True},
    {'title': 'Услуги', 'url': '#services', 'active': True},
    {'title': 'Запись на стрижку', 'url': '#orderForm', 'active': True},
]

class MainPageView(TemplateView):
    template_name = "main.html"
    success_url = 'thanks'
    model = Visit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MENU
        context['masters'] = Master.objects.all()
        context['services'] = Service.objects.all()
        context['form'] = VisitForm
        return context



class ThanksView(TemplateView):
    template_name = 'thanks.html'

    extra_context = {"menu": MENU}