
from rest_framework import status
from rest_framework.response import Response
from datetime import date
from rest_framework.views import APIView
from .models import Project, Labour, Material, Equipment,ResourceUsage
from .serializers import ProjectSerializer,LabourSerializer,MaterialSerializer,EquipmentSerializer,ResourceUsageSerializer

class LabourView(APIView):
    def get(self, request):
        labours = Labour.objects.all()
        serializer = LabourSerializer(labours, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = LabourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        labour = Labour.objects.get(pk=pk)
        serializer = LabourSerializer(labour, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        labour = Labour.objects.get(pk=pk)
        labour.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def delete(self, request, pk):
        try:
         labour = Labour.objects.get(pk=pk)
         serializer=LabourSerializer(labour,many=True)
         return Response(serializer.data)
        except:
         return Response(status=status.HTTP_204_NO_CONTENT)
class EquipmentView(APIView):
    def get(self, request):
        equipments = Equipment.objects.all()
        serializer = EquipmentSerializer(equipments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        equipments = Equipment.objects.get(pk=pk)
        serializer = EquipmentSerializer(equipments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        equipments = Equipment.objects.get(pk=pk)
        equipments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class MaterialView(APIView):

    def post(self,request):
        serializer=MaterialSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        materials = Material.objects.all()
        serializer = MaterialSerializer(materials, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self, request, pk):
        material = Material.objects.get(pk=pk)
        serializer = MaterialSerializer(material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        materials = Material.objects.get(pk=pk)
        materials.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectView(APIView):
    # def get(self, request):
    #     projects = Project.objects.all()
    #     serializer = ProjectSerializer(projects, many=True)
        # return Response(serializer.data)    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            labour_ids = request.data['labour_ids']
            material_ids = request.data['material_ids']
            material_quantities = request.data['material_quantities']
            equipment_ids = request.data['equipment_ids']
            equipment_quantities = request.data['equipment_quantities']
            project = Project.objects.get(id=serializer.data['id'])
            for labour_id in labour_ids:
                labour = Labour.objects.get(id=int(labour_id))
                ResourceUsage.objects.create(project=project, labour=labour, usage_date=date.today(),resource_type='labour')
                # labour.delete()
            for i in range(len(material_ids)):
                material_id = material_ids[i]
                material_quantity = material_quantities[i]
                material = Material.objects.get(id=int(material_id))
                material.quantity -= int(material_quantity)
                material.save()
                ResourceUsage.objects.create(project=project, material=material, usage_quantity=int(material_quantity), usage_date=date.today(), resource_type='material')
                 
            for i in range(len(equipment_ids)):
                equipment_id = equipment_ids[i]
                equipment_quantity = equipment_quantities[i]
                equipment = Equipment.objects.get(id=int(equipment_id))
                equipment.quantity -= int(equipment_quantity)
                equipment.save()
                ResourceUsage.objects.create(project=project, equipment=equipment, usage_quantity=int(equipment_quantity), usage_date=date.today(), resource_type='equipment')
             
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk):
        projects = Project.objects.get(pk=pk)
        projects.delete()
        return Response({"Project Deleted Succesfully"},status=status.HTTP_204_NO_CONTENT)
    def put(self, request, pk):
     project = Project.objects.get(pk=pk)
     serializer = ProjectSerializer(data=request.data)
     if serializer.is_valid():
            serializer.save()
            labour_ids = request.data['labour_ids']
            material_ids = request.data['material_ids']
            material_quantities = request.data['material_quantities']
            equipment_ids = request.data['equipment_ids']
            equipment_quantities = request.data['equipment_quantities']
            project = Project.objects.get(id=serializer.data['id'])
            for labour_id in labour_ids:
                labour = Labour.objects.get(id=int(labour_id))
                labour.allocated(True)
                ResourceUsage.objects.create(project=project, labour=labour, usage_date=date.today(),resource_type='labour')
                # labour.delete()
            for i in range(len(material_ids)):
                material_id = material_ids[i]
                material_quantity = material_quantities[i]
                material = Material.objects.get(id=int(material_id))
                material.quantity -= int(material_quantity)
                material.save()
                ResourceUsage.objects.create(project=project, material=material, usage_quantity=int(material_quantity), usage_date=date.today(), resource_type='material')
            for i in range(len(equipment_ids)):
                equipment_id = equipment_ids[i]
                equipment_quantity = equipment_quantities[i]
                equipment = Equipment.objects.get(id=int(equipment_id))
                equipment.quantity -= int(equipment_quantity)
                equipment.save()
                ResourceUsage.objects.create(project=project, equipment=equipment, usage_quantity=int(equipment_quantity), usage_date=date.today(), resource_type='equipment')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class ResourceUsageView(APIView):
    def get(self, request, project_id):
        resource_usage = ResourceUsage.objects.filter(project_id=project_id)
        serializer = ResourceUsageSerializer(resource_usage, many=True)
        return Response(serializer.data)
    