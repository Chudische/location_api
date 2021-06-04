import json
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse

from .models import Place
from .serializers import SearchFirstLetters

@api_view(['GET'])
def get_name_by_id(request):
    """Return name of place by id """      
    try:
        place = Place.objects.get(pk=request.GET.get('id', ''))
    except ObjectDoesNotExist:
        return Response({'error': 'place with current id does not exist'}, HTTP_404_NOT_FOUND)

    print(place.category)
    responce = {'name': place.name}    
    return Response(responce)


@api_view(['GET'])
def get_full_name_by_id(request):
    """Return name of place with district and region if exist """
    try:       
        place = Place.objects.get(pk=request.GET.get('id', ''))
    except ObjectDoesNotExist:
        return Response({'error': 'place with current id does not exist'}, HTTP_404_NOT_FOUND)           
    
    responce = {'full_name': str(place) + place.get_all_parents()}
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
        responce.append({'full_name': place.name + place.get_all_parents()})
    return Response(responce)


@api_view(['GET'])
def find_full_names(request):
    search_key = request.GET.get('find', '')
    query = Place.objects.filter(category__isnull=False, name__startswith=search_key.upper()).order_by('rating')
    response = []
    for place in query:
        response.append({'name': str(place),
                         'full_name': place.get_all_parents(),
                         'id': place.id})
    return Response(response)


@api_view(['GET'])
def find_names(request):
    search_key = request.GET.get('find', '')
    query = Place.objects.filter(category__isnull=False, name__startswith=search_key.upper()).order_by('rating')
    serializer = SearchFirstLetters(query, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_parents_id(request):
    place = Place.objects.get(pk=request.GET.get('id', ''))
    responce = place.get_parents_id()
    return Response(responce)


@api_view(['GET'])
def get_affiliations_ids_by_id(request):
    place = Place.objects.get(pk=request.GET.get('id', ''))
    responce = place.get_affiliations()
    return Response(responce)

@api_view(['GET'])
def get_name_with_affiliations_by_id(request):
    place = Place.objects.get(pk=request.GET.get('id', ''))
    responce = place.get_name_with_affilations()
    return Response(responce)

@api_view(['GET'])
def get_all_places_ids_in_location_area_by_id(request):
    place = Place.objects.get(pk=request.GET.get('id', ''))
    affil = place.get_affiliations()
    area = Place.objects.get(pk=affil['area'])
    childs_id = area.get_all_childs()
    responce = childs_id
    # for location in childs_area:
    #     childs_location = location.get_childs()
    #     if childs_location:
    #         for
    #     else:
    #     responce.append({'id':location.id, 'name':str(location)})
    return Response(responce)




def all_locations_with_full_name(request):
    all_locations = Place.objects.filter(is_location=True)
    response = '<html><body><h1>Все населенные пункты</h1>'
    for location in all_locations:
        affil = location.get_name_with_affiliations()
        response += "<span>" + str(location.id) +"</span> <b>" + str(location) + "</b> " + affil['area'] + " <i>" + affil['region'] + "</i><br>" 
    response += "<h1>The end</h1></body></html>"
    return HttpResponse(response)

def all_locations_without_area(request):
    all_locations = Place.objects.filter(is_location=True)
    response = '<html><body><h1>Все населенные пункты без районов</h1>'
    for location in all_locations:
        affil = location.get_affiliations()
        if not affil['area']:
            response += "<span>id:" + str(location.id) +"</span> name:<b>" + str(location) + "</b> is null area:" + str(affil['area']) + " <i>region:" + str(affil['region']) + "</i><br>" 
    response += "<h1>The end</h1></body></html>"
    return HttpResponse(response)

def all_locations_without_region(request):
    all_locations = Place.objects.filter(is_location=True)
    response = '<html><body><h1>Все населенные пункты без районов</h1>'
    for location in all_locations:
        affil = location.get_affiliations()
        if not affil['region']:
            response += "<span>id:" + str(location.id) +"</span> name:<b>" + str(location) + "</b>area:" + str(affil['area']) + " <i>region is null:" + str(affil['region']) + "</i><br>" 
    response += "<h1>The end</h1></body></html>"
    return HttpResponse(response)
