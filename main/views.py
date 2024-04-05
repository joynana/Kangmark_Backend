from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import User,Courses_list
from .serializers import UserSerializers ,Courses_listSerializers ,ScheduleSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def user_list(request):

    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializers(user, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def me(request):
    # user = request.user
    user = User.objects.get(id=1) # 로그인 한 것으로 치고, 무조건 user중에 첫번째 값만 가져오기
    serializer = UserSerializers(user)
    return Response(serializer.data)


@api_view(['GET'])
def courses(request):
    # user = request.user
    user = User.objects.get(id=6)
    course_list = user.courses_list_set.all()
    serializer = Courses_listSerializers(course_list, many=True)
    print(course_list)
    # courses = Courses_list.objects.get(id=1) # 로그인 한 것으로 치고, 무조건 user중에 첫번째 값만 가져오기
    # serializer = Courses_listSerializers(courses)
    return Response(serializer.data)

@api_view(['GET'])
def schedule(request):
    # user = request.user
    user = User.objects.get(id=6)
    schedule = user.schedule_set.all()
    serializer = ScheduleSerializers(schedule, many=True)
    print(schedule)
    # courses = Courses_list.objects.get(id=1) # 로그인 한 것으로 치고, 무조건 user중에 첫번째 값만 가져오기
    # serializer = Courses_listSerializers(courses)
    return Response(serializer.data)


