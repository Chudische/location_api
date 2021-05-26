from django.db.models import IntegerField, CharField, Model, BooleanField
from django.contrib.gis.db.models import PointField

class Place(Model):
    CHOISES = [
        ('О', 'ОБЛАСТЬ'),
        ('Р', 'РАЙОН'),
        ('М', 'МІСТО'),
        ('Т', 'СМТ'),
        ('С', 'СЕЛО'),
        ('Щ', 'СЕЛИЩЕ'),
    ]
    id = IntegerField(primary_key=True, verbose_name="Код")
    parent_id = IntegerField(verbose_name="Родитель", db_index=True, null=True)
    category = CharField(max_length=1, choices=CHOISES, verbose_name="Категория")
    name = CharField(max_length=255, verbose_name="Название")
    coordinates = PointField(verbose_name="Координаты", null=True)
    rating = IntegerField(default=0, verbose_name='Рейтинг')
    is_active = BooleanField(default=True, verbose_name='Запись активна?')

    

    def __str__(self):
        return self.name

    def get_full_name(self):
        full_name = self.get_category_display() + ' ' + self.name
        parent_id = self.parent_id       
        while parent_id:
            parent = Place.objects.get(pk=parent_id)
            full_name = parent.name + ' ' + full_name
            parent_id = parent.parent_id            
        return full_name

    def get_coordinates_from_post(self):
        pass

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
