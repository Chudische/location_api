import json
from django.shortcuts import render
from django.utils.translation import to_locale
from django.http import JsonResponse


def get_location_by_name(name):
    """Return location instance by name"""
#получить координаты по названию НП(населенный пункт)
    pass

def set_current_location(location):
#это мне не понятно    
    pass

def get_current_location(location):
#это мне не понятно    
    pass

def get_region_by_location(location):
    """Return region by location"""
#получить район по названию НП?
    pass

def get_district_by_location(location):
    """Return district by location"""
#получить район нп?
    pass

def get_settelments_in_radius(radius):
    """Return all settelments in area 'radius' over current location"""
#settelments? what is? ))
#получить нп в радиусе от НП?

    pass

#мой взгляд на эти вещи ))
def get_name_by_id(request):
#получить название НП по его id\
    if request.method == 'GET' and request.GET: #..../get_name_by_id/?id=11831 или брать из url ..../get_name_by_id/11831/ не помню как делается там в urls.py нужно химичить
        try:
            if 'id' in request.GET:
                id = int(request.GET['id'],16)
                name = 'Скадовск'#TODO сделать обращение к базе и получение названия НП по полученному id
        except:
                raise Http404("id does not exist")            
    responce = {'name':name}
    return JsonResponse(responce)

def get_full_name_by_id(request):
#получить название НП с указанием области и района по его id\
    if request.method == 'GET' and request.GET:
        try:
            if 'id' in request.GET:
                id = int(request.GET['id'],16)
                name = 'Херсонская обл. Скадовский р-н с. Антоновка'#TODO сделать обращение к базе и получение названия НП по полученному id
        except:
                raise Http404("id does not exist")            
    responce = {'full_name':name}
    return JsonResponse(responce)

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
    
    return JsonResponse(responce)
