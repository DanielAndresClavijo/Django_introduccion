from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
  def get(self, request, *args, **kwargs):
    context={
       "var1":1
    }
    return render(request, 'index.html', context)
