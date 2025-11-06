
# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


# def apptest(request):
#    return HttpResponse('my first APWR page')

from django.http import HttpResponse
from django.template import loader

# from . import itemsmng
from .models import Item
from .itemsmng import charger
# import itemsmng

def apptest(request):
  # template = loader.get_template('apwrFirst.html')
  pList = []
  item2add = charger()
  item2add.name = 'charger 1'
  pList.append(item2add.__dict__)
  item2add = charger()
  item2add.name = 'charger 2'
  pList.append(item2add.__dict__)
  #dblist = Item.objects.all()[0]
  template = loader.get_template('apwrMain.html')
  context = {
    'pList':pList,
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


