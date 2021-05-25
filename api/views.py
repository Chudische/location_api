import json
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Place

@api_view(['GET'])
def get_name_by_id(request):
    """Return name of place by id """      
    try:
        place = Place.objects.get(pk=request.GET.get('id', ''))
    except ObjectDoesNotExist:
        return Response({'error': 'place with current id does not exist'}, HTTP_404_NOT_FOUND)

    responce = {'name': place.name}    
    return Response(responce)


@api_view(['GET'])
def get_full_name_by_id(request):
    """Return name of place with district and region if exist """
    try:       
        place = Place.objects.get(pk=request.GET.get('id', ''))
    except ObjectDoesNotExist:
        return Response({'error': 'place with current id does not exist'}, HTTP_404_NOT_FOUND)           
    
    responce = {'full_name': place.get_full_name()}
    return Response(responce)


def get_most_popular_localities_by_names_first_leters(request):
#получить НП (названия и id)  по первым буквам (можно в ответе разбивать на одласть район ...)
    responce = {}
    if request.method == 'GET' and request.GET:
        try:
            if 'flname' in request.GET:
                flname = request.GET['flname']#='ки'
                count = int(request.GET['count'],16)
                responce ={'0':{'id':12,'name':'Киев'},'1':{'id':52351, 'name':'Львовская обл. Стрийский р-н с.Киринеи,'},}#TODO сделать обращение к базе и получение названий колличество ограничить параметром count
        except:
                raise Http404("flname or count does not exist")            
    
    return JsonResponse(json.dumps(responce, ensure_ascii=False, default=str), safe=False)
