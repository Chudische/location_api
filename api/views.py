import json
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Place
from .serializers import SearchFirstLetters

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

@api_view(['GET'])
def get_ids_by_name(request):
    """Return id by name of place TODO: sort by raiting"""
    try:
        get_name = request.GET.get('name', '')
        #text_name = get_name.text
        upper_name = get_name.upper()
        print(upper_name)
        places = Place.objects.filter(name=upper_name)
    except ObjectDoesNotExist:
        return Response({'error': 'place with current name does not exist'}, HTTP_404_NOT_FOUND)           
    responce = []
    for place in places:
        responce.append({'id': place.id})

    print (responce)
    return Response(responce)

@api_view(['GET'])
def get_full_names_by_name(request):
    """Return full names by name of place TODO: sort by raiting"""
    try:
        get_name = request.GET.get('name', '')
        #text_name = get_name.text
        upper_name = get_name.upper()
        print(upper_name)
        places = Place.objects.filter(name=upper_name)
    except ObjectDoesNotExist:
        return Response({'error': 'place with current name does not exist'}, HTTP_404_NOT_FOUND)           
    responce = []
    for place in places:
        responce.append({'full_name': place.get_full_name()})

    print (responce)
    return Response(responce)


@api_view(['GET'])
def find_full_names(request):
    search_key = request.GET.get('find', '')
    query = Place.objects.filter(category__isnull=False, name__startswith=search_key.upper())
    response = []
    for place in query:
        response.append({'name': place.get_full_name(),
                         'id': place.id})
    return Response(response)

@api_view(['GET'])
def find_names(request):
    search_key = request.GET.get('find', '')
    query = Place.objects.filter(category__isnull=False, name__startswith=search_key.upper())
    serializer = SearchFirstLetters(query, many=True)
    return Response(serializer.data)


def get_most_popular_localities_by_names_first_leters(request):
    """ """
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
