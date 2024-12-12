
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project, Labour, Material, Equipment
from .serializers import ProjectSerializer,LabourSerializer,MaterialSerializer,EquipmentSerializer

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
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
 
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            labour_ids = request.data['labour_ids']
            material_id = request.data['material_id']
            material_quantity = request.data['material_quantity']
            equipment_id = request.data['equipment_id']
            equipment_quantity = request.data['equipment_quantity']

            for labour_id in labour_ids:
                labour = Labour.objects.get(id=int(labour_id))
                labour.allocated = True
                labour.delete()

            for material, quantity in zip(material_id, material_quantity):
                material= Material.objects.get(id=int(material))
                material.quantity -= int(quantity)
                material.save()

            for equipment, quantity in zip(equipment_id, equipment_quantity):
                equipment= Equipment.objects.get(id=int(equipment))
                equipment.quantity -= int(quantity)
                equipment.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        projects = Project.objects.get(pk=pk)
        projects.delete()
        return Response({"Project Deleted Succesfully"},status=status.HTTP_204_NO_CONTENT)
    def put(self, request, pk):
     project = Project.objects.get(pk=pk)
     serializer = ProjectSerializer(project, data=request.data)
     if serializer.is_valid():
        serializer.save()
        labour_ids = request.data['labour_ids']
        material_id = request.data['material_id']
        material_quantity = request.data['material_quantity']
        equipment_id = request.data['equipment_id']
        equipment_quantity = request.data['equipment_quantity']

        
        for labour_id in labour_ids:
            labour = Labour.objects.get(id=int(labour_id))
            labour.allocated = True
            labour.save()

        
        for material, quantity in zip(material_id, material_quantity):
            material_obj = Material.objects.get(id=int(material))
            material_obj.quantity -= int(quantity)
            material_obj.save()

        for equipment, quantity in zip(equipment_id, equipment_quantity):
            equipment_obj = Equipment.objects.get(id=int(equipment))
            equipment_obj.quantity -= int(quantity)
            equipment_obj.save()

        return Response(serializer.data)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

    