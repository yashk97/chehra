from ..models import Student, StudentImage, Teacher
from rest_framework.serializers import ModelSerializer
from ..models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'user', 'uid', 'dept_id']


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['teacher_id', 'user']


class StudentImageSerializer(ModelSerializer):
    class Meta:
        model = StudentImage
        fields = ['image_id', 'student_id', 'image', 'type']
