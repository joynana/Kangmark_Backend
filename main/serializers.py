from rest_framework import serializers
from .models import User, Courses, Categories, Courses_list, Schedule

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","name")


class CoursesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ("name","url","img")
        # fields = '__all__'


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ("categories_name",)


class Courses_listSerializers(serializers.ModelSerializer):
    category = CategoriesSerializers()
    course = CoursesSerializers()
    class Meta:
        model = Courses_list
        # fields = ("categories_name","name","url","img")
        fields = ("category","course")

class ScheduleSerializers(serializers.ModelSerializer):

    class Courses_listSerializers(serializers.ModelSerializer):
        
        class CoursesSerializers(serializers.ModelSerializer):
            class Meta:
                model = Courses
                fields = ("name",)
                # fields = '__all__'

        course = CoursesSerializers()
        class Meta:
            model = Courses_list
            fields = ("course",)

    courses_list = Courses_listSerializers()
    class Meta:
        model = Schedule
        # fields = ("categories_name","name","url","img")
        fields = ("start_time","courses_list",)
    
    # class Meta:
    #     model = Schedule
    #     fields = ("categories_name",)