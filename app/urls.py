from django.urls import path
from app.views import *

urlpatterns = [
    path('projects/', GetProjectView.as_view()),
    path('projects/<int:pk>/', ProjectView.as_view()),
    path('labours/', LabourView.as_view()),
    path('labours/<int:pk>/',LabourView.as_view()),
    path('equipments/',EquipmentView.as_view()),
    path('equipments/<int:pk>/',EquipmentView.as_view()),
    path('materials/<int:pk>/',MaterialView.as_view()),
    path('materials/',MaterialView.as_view()),
     path('projects/<int:project_id>/resource-usage/',ResourceUsageView.as_view()),

]