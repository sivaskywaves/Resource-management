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
    material_ids = models.CharField(max_length=255)
    material_quantities = models.CharField(max_length=255)
    equipment_ids = models.CharField(max_length=255)
    equipment_quantities = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class ResourceUsage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    labour = models.ForeignKey(Labour, on_delete=models.CASCADE, null=True, blank=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, null=True, blank=True)
    usage_date = models.DateField()
    usage_quantity = models.IntegerField(null=True, blank=True)
    resource_type = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.project.name} - {self.resource_type}"

