from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    labour_ids = serializers.ListField(child=serializers.IntegerField())
    material_id = serializers.ListField(child=serializers.IntegerField())
    material_quantity = serializers.ListField(child=serializers.IntegerField())
    equipment_id = serializers.ListField(child=serializers.IntegerField())
    equipment_quantity = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        model = Project
        fields = ['id', 'name', 'labour_ids', 'material_id', 'material_quantity', 'equipment_id', 'equipment_quantity']   
 
    

class LabourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labour
        fields = ['id', 'name','profession','profession_name','allocated']

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name', 'quantity']

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name', 'quantity','units']
        
class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id', 'name']
class ProjectSerializer(serializers.ModelSerializer):
    labour_ids = serializers.ListField(child=serializers.IntegerField())
    material_ids = serializers.ListField(child=serializers.IntegerField())
    material_quantities = serializers.ListField(child=serializers.IntegerField())
    equipment_ids = serializers.ListField(child=serializers.IntegerField())
    equipment_quantities = serializers.ListField(child=serializers.IntegerField())
    class Meta:
        model = Project
        fields = ['id', 'name', 'labour_ids', 'material_ids', 'material_quantities', 'equipment_ids', 'equipment_quantities']
        def get_labour_ids(self, obj):
         return obj.labour_ids.split(',')

        def get_material_ids(self, obj):
         return obj.material_ids.split(',')

        def get_material_quantities(self, obj):
         return obj.material_quantities.split(',')

        def get_equipment_ids(self, obj):
         return obj.equipment_ids.split(',')

        def get_equipment_quantities(self, obj):
         return obj.equipment_quantities.split(',')


class ResourceUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceUsage
        fields = ['id', 'project', 'labour', 'material', 'equipment', 'usage_date', 'usage_quantity']
