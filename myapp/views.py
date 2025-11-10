
# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


# def apptest(request):
#    return HttpResponse('my first APWR page')

from django.http import HttpResponse
from django.template import loader

import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect

# from . import itemsmng
from .models import Item
from .itemsmng import charger
# import itemsmng

@require_POST
@csrf_protect
def receive_text_data(request):
  try:
    # Load the JSON body
    data = json.loads(request.body)

    # Access the specific key sent by the JavaScript
    received_text = data.get('input_text', 'No text provided')

    # --- Print the data to the console for verification ---
    print(f"\n--- SERVER RECEIVED TEXT ---")
    print(f"Received characters: {received_text}")
    print(f"Length: {len(received_text)}")
    print(f"---------------------------\n")

    # Send a success response back to the JavaScript
    return JsonResponse({
      'status': 'success',
      'message': f'Server received your text: "{received_text[:20]}..." ({len(received_text)} chars)'
    })

  except json.JSONDecodeError:
    return JsonResponse({'status': 'error', 'message': 'Invalid JSON format.'}, status=400)
  except Exception as e:
    return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


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


