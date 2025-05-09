from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import HospitalSerializer
from hospital.models import Hospital_Information, Patient, User 
from doctor.models import Doctor_Information

@api_view(['GET'])
def getRoutes(request):
    
    
    routes = [
        {'GET': '/api/hospital/'},
        {'GET': '/api/hospital/id'},
        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]
    return Response(routes)

@api_view(['GET'])
def getHospitals(request):
    hospitals = Hospital_Information.objects.all() 
    serializer = HospitalSerializer(hospitals, many=True) 
   
    return Response(serializer.data)


@api_view(['GET'])
def getHospitalProfile(request, pk):
    hospitals = Hospital_Information.objects.get(hospital_id=pk)
    serializer = HospitalSerializer(hospitals, many=False) 
    return Response(serializer.data)
