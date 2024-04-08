from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import User,Courses_list,KangMark
from .serializers import UserSerializers ,Courses_listSerializers ,ScheduleSerializers ,duration_timeSerializers,SubjectsSerializers,Due_dateSerializers,KangmarkSerializers
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
    user = User.objects.get(id=1)
    course_list = user.courses_list_set.all()
    serializer = Courses_listSerializers(course_list, many=True)
    # print(course_list)
    # courses = Courses_list.objects.get(id=1) # 로그인 한 것으로 치고, 무조건 user중에 첫번째 값만 가져오기
    # serializer = Courses_listSerializers(courses)
    from collections import defaultdict
    dic = defaultdict(list)
    for data in serializer.data:
        # 카테고리 가져오기
        category = data.get('category').get('categories_name')

        # 입력할 데이터에서 카테고리 삭제하기 (key값으로 뺐기 때문에)
        del data['category']
        # course로 1depth 들어간거 빼주기
        dic[category].append(data.get('course'))
    return Response(dic)
    return Response(serializer.data)

@api_view(['GET'])
def schedule(request):
    # user = request.user
    user = User.objects.get(id=1)
    schedule = user.schedule_set.all()
    serializer = ScheduleSerializers(schedule, many=True)
    print(schedule)
    # courses = Courses_list.objects.get(id=1) # 로그인 한 것으로 치고, 무조건 user중에 첫번째 값만 가져오기
    # serializer = Courses_listSerializers(courses)
    return Response(serializer.data)



@api_view(['GET'])
def duration_time(request):
    # user = request.user
    user = User.objects.get(id=1)
    schedule = user.schedule_set.all()
    serializer = duration_timeSerializers(schedule, many=True)
    print(schedule)
    # courses = Courses_list.objects.get(id=1) # 로그인 한 것으로 치고, 무조건 user중에 첫번째 값만 가져오기
    # serializer = Courses_listSerializers(courses)
    return Response(serializer.data)

@api_view(['GET'])
def subjects(request):
    # user = request.user
    user = User.objects.get(id=1)
    schedule = user.schedule_set.all()
    serializer = SubjectsSerializers(schedule, many=True)
    print(schedule)
    # courses = Courses_list.objects.get(id=1) # 로그인 한 것으로 치고, 무조건 user중에 첫번째 값만 가져오기
    # serializer = Courses_listSerializers(courses)
    return Response(serializer.data)


@api_view(['GET'])
def due_date(request):
    # user = request.user
    user = User.objects.get(id=1)
    course_list = user.courses_list_set.all()
    serializer = Due_dateSerializers(course_list, many=True)
    print(course_list)
    # courses = Courses_list.objects.get(id=1) # 로그인 한 것으로 치고, 무조건 user중에 첫번째 값만 가져오기
    # serializer = Courses_listSerializers(courses)
    return Response(serializer.data)

@api_view(['GET'])

def kangmark(request):
    user = User.objects.get(id=1)
    kangmark = user.kangmark_set.all()
    serializer = KangmarkSerializers(kangmark, many=True)
    print(kangmark)
    return Response(serializer.data)