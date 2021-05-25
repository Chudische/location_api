import json
from rest_framework.decorators import api_view
from django.http import JsonResponse


def get_name_by_id(request):
#получить название НП по его id\
    if request.method == 'GET' and request.GET: #..../get_name_by_id/?id=11831 или брать из url ..../get_name_by_id/11831/ не помню как делается там в urls.py нужно химичить
        try:
            if 'id' in request.GET:
                id = int(request.GET['id'],16)
                name = 'Скадовск'#TODO сделать обращение к базе и получение названия НП по полученному id
        except:
                raise Http404("id does not exist")            
    responce = {'name': name}
    
    return JsonResponse(responce, safe=False)

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
    return JsonResponse(json.dumps(responce, ensure_ascii=False, default=str), safe=False)

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
