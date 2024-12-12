from rest_framework import serializers
from .models import Project,Labour,Equipment,Material,Profession

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