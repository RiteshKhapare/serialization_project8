from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    e_id = serializers.IntegerField()
    e_name = serializers.CharField()
    age = serializers.IntegerField()
    sal = serializers.IntegerField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.e_id = validated_data.get('e_id', instance.e_id)
        instance.e_name = validated_data.get('e_name', instance.e_name)
        instance.age = validated_data.get('age', instance.age)
        instance.sal = validated_data.get('sal', instance.sal)
        instance.save()
        return instance