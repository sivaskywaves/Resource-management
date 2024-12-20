from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from django.core.mail import send_mail
from datetime import date
from rest_framework.views import APIView
from .models import Project, Labour, Material, Equipment,ResourceUsage
from .serializers import ProjectSerializer,LabourSerializer,MaterialSerializer,EquipmentSerializer,ResourceUsageSerializer
class LaboursView(APIView):
   def post(self, request):
        serializer = LabourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   def  get(self,request):
      labours=Labour.objects.all()
      serializer=LabourSerializer(labours,many=True)
      return Response(serializer.data)
class LabourView(APIView):
    def get(self, request, pk):
     try:
        labour = Labour.objects.get(pk=pk)
        serializer = LabourSerializer(labour)
        return Response(serializer.data)
     except Equipment.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        labour = Labour.objects.get(pk=pk)
        serializer = LabourSerializer(labour, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
         labour = Labour.objects.get(pk=pk)
         labour.delete()
         return Response("Deleted Succesfully")
        except:
         return Response(status=status.HTTP_204_NO_CONTENT)
class EquipmentsView(APIView):
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
   
           
class EquipmentView(APIView):
    
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
    def get(self, request, pk):
     try:
        equipment = Equipment.objects.get(pk=pk)
        serializer = EquipmentSerializer(equipment)
        return Response(serializer.data)
     except Equipment.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
class MaterialsView(APIView):
   
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


class MaterialView(APIView):

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
    def get(self, request, pk):
     try:
        material = Material.objects.get(pk=pk)
        serializer = MaterialSerializer(material)
        return Response(serializer.data)
     except Equipment.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

class ProjectView(APIView):
    def get(self, request,pk):
        project = Project.objects.get(pk=pk)
        data = []
        labour_ids = project.labour_ids.split(',')
        material_ids = project.material_ids.split(',')
        material_quantities = project.material_quantities.split(',')
        equipment_ids = project.equipment_ids.split(',')
        equipment_quantities = project.equipment_quantities.split(',')
        data.append({
                'project_id':project.id,
                'project_name': project.name,
                'labour_ids': labour_ids,
                'material_ids': material_ids,
                'material_quantities': material_quantities,
                'equipment_ids': equipment_ids,
                'equipment_quantities': equipment_quantities
            })
        return Response(data) 
    


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
                labour.delete()
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
class ResourcesUsageView(APIView):
    def get(self,request):
        usage=ResourceUsage.objects.all()
        serializer=ResourceUsageSerializer(usage,many=True)
        return Response(serializer.data)
class ProjectsView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        data = []
        for project in projects:
            labour_ids = project.labour_ids.split(',')
            material_ids = project.material_ids.split(',')
            material_quantities = project.material_quantities.split(',')
            equipment_ids = project.equipment_ids.split(',')
            equipment_quantities = project.equipment_quantities.split(',')
            data.append({
                'project_id':project.id,
                'project_name': project.name,
                'labour_ids': labour_ids,
                'material_ids': material_ids,
                'material_quantities': material_quantities,
                'equipment_ids': equipment_ids,
                'equipment_quantities': equipment_quantities
            })
        return Response(data)
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
                if material.quantity < int(material_quantity):
                    send_mail(
                        'Resources are less than required',
                        f'Material {material.name} is less than required for project {project.name}',
                        'your mail@gmail.com',#ours mail
                        ['admin@gmail.com'],#admin
                        fail_silently=False,
                    )
                    return Response({'message': f'Resources are less than required for project {project.name}'}, status=status.HTTP_200_OK)
                else:
                   material.quantity -= int(material_quantity)
                   material.save()
                   ResourceUsage.objects.create(project=project, material=material, usage_quantity=int(material_quantity), usage_date=date.today(), resource_type='material')
                 
            for i in range(len(equipment_ids)):
                equipment_id = equipment_ids[i]
                equipment_quantity = equipment_quantities[i]
                equipment = Equipment.objects.get(id=int(equipment_id))
                if equipment.quantity < int(equipment_quantity):
                    
                    send_mail(
                        'Resources are less than required',
                        f'Equipment {equipment.name} is less than required for project {project.name}',
                        'your mail',#ours mail
                        ['admin@gmail.com'],#admin
                        
                        fail_silently=False,
                    )
                    return Response({'message': f'Resources are less than required for project {project.name}'}, status=status.HTTP_200_OK)
                else:
                  equipment.quantity -= int(equipment_quantity)
                  equipment.save()
                  ResourceUsage.objects.create(project=project, equipment=equipment, usage_quantity=int(equipment_quantity), usage_date=date.today(), resource_type='equipment')
             
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
