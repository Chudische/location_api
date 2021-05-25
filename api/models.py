from django.db.models import IntegerField, CharField, Model
from django.contrib.gis.db.models import PointField

class Place(Model):
    CHOISES = [
        ('О', 'область'),
        ('Р', 'район'),
        ('М', 'місто'),
        ('Т', 'смт'),
        ('С', 'село'),        
        ('Щ', 'селище'),
    ]
    id = IntegerField(primary_key=True, verbose_name="Код")
    parent_id = IntegerField(verbose_name="Родитель", db_index=True, null=True)
    category = CharField(max_length=1, choices=CHOISES, verbose_name="Категория")
    name = CharField(max_length=255, verbose_name="Название")
    coordinates = PointField(verbose_name="Координаты", null=True)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'
 
