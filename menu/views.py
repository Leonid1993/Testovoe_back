from django.shortcuts import render
from django.views.generic import View

class BaseView(View):
    def get(self, request, slug):
        return render(request, 'base.html')


