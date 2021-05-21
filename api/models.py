from shabashka.main.models import Category
from shabashka.main.views import index
from django.db import models


class Place(models.Model):
    CHOISES = [
        ('О', 'область'),
        ('Р', 'район'),
        ('М', 'місто'),
        ('Т', 'смт'),
        ('С', 'село'),        
        ('Щ', 'селище'),
    ]
    id = models.IntegerField(primary_key=True, verbose_name="Код")
    parent_id = models.IntegerField(verbose_name="Родитель", db_index=True, null=True)
    category = models.CharField(max_length=1, choices=CHOISES, verbose_name="Категория")
    name = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'
 