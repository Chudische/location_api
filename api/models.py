from django.db.models import IntegerField, CharField, Model, BooleanField
from django.contrib.gis.db.models import PointField


class Place(Model):
    CHOISES = [
        ('О', 'обл. '),
        ('РГ', 'р-н '),
        ('РН', 'р-н '),
        ('М', 'м. '),
        ('Т', 'смт. '),
        ('С', 'с. '),
        ('Щ', 'с. '),
    ]
    id = IntegerField(primary_key=True, verbose_name="Код")
    parent_id = IntegerField(verbose_name="Родитель", db_index=True, null=True, blank=True,)
    category = CharField(max_length=2, choices=CHOISES, null=True, blank=True, verbose_name="Категория")
    name = CharField(max_length=255, verbose_name="Название")
    coordinates = PointField(verbose_name="Координаты", null=True, blank=True)
    rating = IntegerField(default=0, verbose_name='Рейтинг')
    is_location = BooleanField(default=False, verbose_name='Это НП?')
    is_active = BooleanField(default=True, verbose_name='Запись активна?')

    def __str__(self):
        name = self.name.capitalize()
        if name.endswith("район"):
            name = name.replace("район", "р-н")
        elif name.endswith("область"):
            name = name.replace("область", "обл.")
        elif ' ' in name:
            name = ' '.join([word.capitalize() for word in name.split()])
        elif '-' in self.name:
            name = '-'.join([word.capitalize() for word in name.split('-')])
        elif self.get_category_display():
            name = self.get_category_display() + name
        return name

    def all_parents(self):
        all_parents = []
        parent_id = self.parent_id       
        while parent_id:
            parent = Place.objects.get(pk=parent_id)
            all_parents.append(parent)
            parent_id = parent.parent_id            
        return all_parents

    def all_parents_name(self):
        return ' '.join(str(name) for name in self.all_parents())

    def get_affiliations(self):
        region = 0
        area = 0
        parent_id = self.parent_id       
        while parent_id:
            parent = Place.objects.get(pk=parent_id)
            if "РАЙОН" in parent.name:
                area = parent.id
            if parent.category == 'О':
                region = parent.id
            parent_id = parent.parent_id            

        return {'region': region, 'area': area}
    
    def get_name_with_affiliations(self):
        affil = self.get_affiliations()
        try:
            area = str(Place.objects.get(pk=affil['area']))
        except:
            area = ""
        try:
            region = str(Place.objects.get(pk=affil['region']))
        except:
            region = ""

        full_name = {
            'name': str(self),
            'area': area,
            'region': region,
        }
        return full_name

    def full_name(self):
        nwa = self.get_name_with_affiliations()
        return nwa['name'] + ' ' + nwa['area'] + ' ' + nwa['region']

    def get_children(self):
        return Place.objects.filter(parent_id=self.id)

    def get_all_children(self):#TODO:set a maximum deep
        children_id=[]
        children = self.get_children()
        for child in children:
            if not child.get_children():
                if child.is_location:
                    children_id.append({'id': child.id, 'name': str(child)})
            else:
                children_id.extend(child.get_all_children())
        return children_id

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'


class Post(Model):
    region = CharField(max_length=255, verbose_name="Область")
    area = CharField(max_length=255, verbose_name="Район")
    place = CharField(max_length=255, verbose_name="Населенный пункт")
    post_index = CharField(max_length=5, verbose_name="Индекс отделения")
    street = CharField(max_length=255, verbose_name="Улица")
    houses = CharField(max_length=2000, verbose_name="Дома")
    #coordinates = PointField(null=True, verbose_name="Координаты") #или двумя параметрами широта долгота FloatField

    def __str__(self):
        return self.place

    def import_from_csv():
        #проще наверно import_export использовать, или можно свой сдесь написать
        pass

    class Meta:
        verbose_name = 'База данных почты'
        verbose_name_plural = 'База данных почты'
