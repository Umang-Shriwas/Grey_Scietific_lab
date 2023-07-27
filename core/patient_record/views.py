from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from accounts.permissions import UserIsDoctor
from accounts.permissions import UserIsPatient
from .models import Department, PatientRecords
from .serializers import  DepartmentSerializer, PatientRecordsSerializer
from accounts.serializers import *
from rest_framework.views import APIView
from accounts.authentication import MultiTokenAuthentication



class Doctor_listAPI(APIView): 
    authentication_classes =[MultiTokenAuthentication] 
    permission_classes = [UserIsDoctor]     
    def get(self, request): 
        try:  
            doctors = CustomUser.objects.filter(user_type="Doctor")
            
            serializer = CustomUserSerializer(doctors, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e: 
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([MultiTokenAuthentication])
@permission_classes([UserIsDoctor])
def doctor_detail(request, pk):
    try:
        doctor = CustomUser.objects.get(pk=pk,user_type="Doctor")
    except CustomUser.DoesNotExist:
        return Response({'msg': 'Doctor not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomUserSerializer(doctor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomUserSerializer(doctor, data=request.data ,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'update successfully.'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Patient_listAPI(APIView): 
    authentication_classes =[MultiTokenAuthentication] 
    permission_classes = [UserIsDoctor]     
    def get(self, request): 
        try:  
            patient = CustomUser.objects.filter(user_type="Patient")
            serializer = CustomUserSerializer(patient, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e: 
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([MultiTokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def patient_detail(request, pk):
    try:
        patient = CustomUser.objects.get(pk=pk,user_type="Patient")
    except CustomUser.DoesNotExist:
        return Response({'msg': 'Patient not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomUserSerializer(patient)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomUserSerializer(patient, data=request.data ,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'update successfully.'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
@authentication_classes([MultiTokenAuthentication])
@permission_classes([UserIsDoctor])
def patient_records_list(request):
    if request.method == 'GET':
        patient_records = PatientRecords.objects.filter(patient_id__user_type="Patient")
        serializer = PatientRecordsSerializer(patient_records, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print("::::::::::",request.data)
        id=request.data.get('patient_id')
        print(":::::",id)
        patient=CustomUser.objects.get(id=id)
        print("::::::::::::::::::::::::::::",patient)
        print("::::::::::::::::::::::::::::",patient.user_type)
        if patient.user_type == 'Patient':
            print('ok::::::::::ok')
            serializer = PatientRecordsSerializer(data=request.data)
            if serializer.is_valid():
                
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({'msg':"this is not a patient"},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([MultiTokenAuthentication])
@permission_classes([UserIsDoctor,UserIsPatient])
def patient_records_detail(request, pk):
    try:
        patient = PatientRecords.objects.get(pk=pk,patient_id__user_type="Patient")
    except PatientRecords.DoesNotExist:
        return Response({'msg': 'Patient not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientRecordsSerializer(patient)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PatientRecordsSerializer(patient, data=request.data ,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'update successfully.'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class Department_listAPI(APIView): 
    authentication_classes =[MultiTokenAuthentication]    
    def get(self, request): 
        try:  
            department = Department.objects.all()
            serializer = DepartmentSerializer(department, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e: 
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        id=request.data.get('user_id')
        doctor=CustomUser.objects.get(id=id)
        if doctor.user_type == 'Doctor':
            serializer = DepartmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
        
@api_view(['GET', 'PUT'])
@authentication_classes([MultiTokenAuthentication])
@permission_classes([UserIsDoctor])
def department_detail_doctor(request, pk):
    try:
        department = Department.objects.get(pk=pk)
        doctors = CustomUser.objects.filter(user_type='Doctor', department=department)
        
    except Department.DoesNotExist:
        return Response({'detail': 'Department not found.'}, status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        print('::::::',request.data)
        serializer = CustomUserSerializer(doctors,many=True)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # Assuming you want to update the department for all doctors in the department
        new_department_id = request.data.get('new_department_id', None)
        if new_department_id is None:
            return Response({'detail': 'Invalid request data. Missing new_department_id.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            new_department = Department.objects.get(pk=new_department_id)
        except Department.DoesNotExist:
            return Response({'detail': 'New department not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Update department for all doctors in the department
        doctors = CustomUser.objects.filter(user_type='Doctor', department=department)
        for doctor in doctors:
            doctor.department = new_department
            doctor.save()

        return Response({'detail': 'Department updated for all doctors in the department.'}, status=status.HTTP_200_OK)
    


@api_view(['GET', 'PUT'])
@authentication_classes([MultiTokenAuthentication])
@permission_classes([UserIsDoctor])
def department_detail_patient(request, pk):
    try:
        department = Department.objects.get(pk=pk)
        patients = CustomUser.objects.filter(user_type='Patient', department=department)
        
    except Department.DoesNotExist:
        return Response({'detail': 'Department not found.'}, status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        print('::::::',request.data)
        serializer = CustomUserSerializer(patients,many=True)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # Assuming you want to update the department for all doctors in the department
        new_department_id = request.data.get('new_department_id', None)
        if new_department_id is None:
            return Response({'detail': 'Invalid request data. Missing new_department_id.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            new_department = Department.objects.get(pk=new_department_id)
        except Department.DoesNotExist:
            return Response({'detail': 'New department not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Update department for all doctors in the department
        patients = CustomUser.objects.filter(user_type='Patient', department=department)
        for patient in patients:
            patient.department = new_department
            patient.save()

        return Response({'detail': 'Department updated for all patients in the department.'}, status=status.HTTP_200_OK)
    

        
        


    








