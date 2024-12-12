from django.db import models
from django.db import models
class Profession(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Labour(models.Model):
    name = models.CharField(max_length=255)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    profession_name = models.CharField(max_length=255, blank=True)
    allocated = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    units=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    labour_ids = models.CharField(max_length=255)
    material_id = models.CharField(max_length=255)
    material_quantity = models.CharField(max_length=255)
    equipment_id = models.CharField(max_length=255)
    equipment_quantity = models.CharField(max_length=255)

    def __str__(self):
        return self.name