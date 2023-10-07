from django.views import View
from django.shortcuts import render

class IndexView(View):
    def get(self, request):
        template = 'core/index.html'
        return render(request, template)