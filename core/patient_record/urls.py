from django.urls import path
from .views import *

urlpatterns = [
    path('doctors',Doctor_listAPI.as_view(),name='Doctors'),
    path('doctors/<int:pk>',doctor_detail,name='Doctors'),
    path('patients',Patient_listAPI.as_view(),name='Patients'),
    path('patients/<int:pk>',patient_detail,name='Patients'),
    path('patient_records',patient_records_list,name='Patient_Records'),
    path('patinet_records/<int:pk>',patient_records_list,name='Patient_Records'),
    path('departments',Department_listAPI.as_view(),name="Department"),
    path('department/<int:pk>/doctors',department_detail_doctor,name="Department"),
    path('department/<int:pk>/patient',department_detail_patient,name="Department"),
    
]
