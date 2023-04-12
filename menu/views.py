from django.shortcuts import render
from django.views.generic import View

class BaseView(View):
    def get(self, request):
        context = {'context': 'some content'}
        return render(request, 'base.html', context=context)


