from enroll.models import Student
from .serializers import StudentSLR
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSLR
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]