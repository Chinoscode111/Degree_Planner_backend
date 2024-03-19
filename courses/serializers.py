from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'code', 'tag', 'semester', 'credits']

    def validate(self, data):
        """
        Validate that semester and credits are greater than 0.
        """
        credits = data.get('credits')

        if credits <= 0:
            raise serializers.ValidationError("Credits must be greater than 0.")

        return data

