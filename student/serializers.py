from rest_framework import serializers
from .models import School, Student
from django.db.models import Count
class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ["id","name", "max_student", "location"]
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ["id","school", "firstname", "lastname", "identification"]
    def schoolFull(self, school):
        raise serializers.ValidationError(school.name + "school is full.")

    def validation(self, data):
        school = data['school']
        print (Student.objects.filter(school=school.id).count())
        print (school.max_student)
        if method == 'POST' and Student.objects.filter(school=school).count() >= school.max_student:
            self.schoolFull=(school)
        return data
        print(data)
