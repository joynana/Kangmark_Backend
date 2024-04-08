from django.db import models
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=10)
    telephone_num = models.IntegerField()
    school = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
            return self.name
    

class Courses(models.Model):
    name = models.CharField(max_length=10)
    url= models.URLField(max_length=100)
    img = models.ImageField(upload_to='images/')
    subject = models.CharField(max_length=10)
    price = models.IntegerField()
    duration_day = models.IntegerField()



class Categories(models.Model):
    # 유저 id  FK로 들어가야 함
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    categories_name = models.CharField(max_length=10)


#수강내역 #MTON 필드로 들어가야 하는지 궁금하다?
class Courses_list(models.Model):
    # 유저 id  FK로 들어가야 함
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    category= models.ForeignKey(Categories, on_delete=models.CASCADE)
    course= models.ForeignKey(Courses, on_delete=models.CASCADE)
    due_date = models.DateTimeField(auto_now=False)


class Schedule(models.Model):
    # 유저 id  FK로 들어가야 함
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    courses_list= models.ForeignKey(Courses_list, on_delete=models.CASCADE)
    start_time= models.TimeField(auto_now=False)
    end_time = models.TimeField(auto_now=False)


class KangMark(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    url= models.URLField(max_length=100)
    img = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    category= models.ForeignKey(Categories, on_delete=models.CASCADE)
   