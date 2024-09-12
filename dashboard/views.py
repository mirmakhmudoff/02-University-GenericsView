from rest_framework import generics
from .models import Faculty, Group, Kafedra, Subject, Teacher, Student
from .serializers import (
    FacultySerializer, GroupSerializer, KafedraSerializer,
    SubjectSerializer, TeacherSerializer, StudentSerializer
)


class FacultyList(generics.ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyDetail(generics.RetrieveAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class GroupList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class KafedraList(generics.ListAPIView):
    queryset = Kafedra.objects.all()
    serializer_class = KafedraSerializer


class KafedraDetail(generics.RetrieveAPIView):
    queryset = Kafedra.objects.all()
    serializer_class = KafedraSerializer


class SubjectList(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetail(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class TeacherList(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetail(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
