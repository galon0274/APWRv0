
# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


# def apptest(request):
#    return HttpResponse('my first APWR page')

from django.http import HttpResponse
from django.template import loader
from .models import Item

def apptest(request):
  # template = loader.get_template('apwrFirst.html')
  dblist = Item.objects.all()[0]
  template = loader.get_template('apwrMain.html')
  context = {
    'dblist':dblist,
  }
  return HttpResponse(template.render(context,request))

def first(request):
  template = loader.get_template('apwrFirst.html')
  # dblist = Item.objects.all()[0]
  #template = loader.get_template('apwrMain.html')
  # context = {
  #  'dblist':dblist,
  # }
  return HttpResponse(template.render())


