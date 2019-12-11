from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'base.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,{})