from django.urls import path
from app.views import *

urlpatterns = [
    path('projects/', ProjectsView.as_view()),
    path('projects/<int:pk>/', ProjectView.as_view()),
    path('labours/', LaboursView.as_view()),
    path('labours/<int:pk>/',LabourView.as_view()),
    path('equipments/',EquipmentsView.as_view()),
    path('equipments/<int:pk>/',EquipmentView.as_view()),
    path('materials/<int:pk>/',MaterialView.as_view()),
    path('materials/',MaterialsView.as_view()),
    path('projects/<int:project_id>/resource-usage/',ResourceUsageView.as_view()),
    path('projects/resource-usage/',ResourcesUsageView.as_view()),


]