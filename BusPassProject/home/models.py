from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class College(models.Model):
    college_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    name = name = models.CharField(max_length=30)
    e_sign = models.ImageField(upload_to='home/e_sign', default="" )

class Route(models.Model):
    route_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    fathername = models.CharField(max_length=30)
    college = models.ForeignKey(College,related_name='%(class)s_requests_created',on_delete=models.CASCADE)
    roll = models.PositiveIntegerField()
    course = models.CharField(max_length=30)
    aadhar_photo = models.ImageField(upload_to='home/aadhar_photo', default="" )
    aadhar_number = models.PositiveIntegerField(null=True)
    previous_pass = models.BooleanField(default=True)
    pass_number = models.CharField(max_length=30, default="")
    route_from = models.ForeignKey(Route,related_name='%(class)s_from_created',on_delete=models.CASCADE ,null=True )
    route_to = models.ForeignKey(Route,related_name='%(class)s_to_created',on_delete=models.CASCADE, null=True)
    verify_college = models.BooleanField(default=False)
    verify_college_reject = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='home/profile_photo', default="" )
    current_pass = models.BooleanField(default=False)
    valid_from = models.DateField(null=True)
    valid_to = models.DateField(null=True)
    price = models.PositiveIntegerField(null=True)
    verify_manager = models.BooleanField(default=False)
    verify_manager_reject = models.BooleanField(default=False)
    phone = models.PositiveIntegerField(null=True)
    apply = models.BooleanField(default=False)

class Pass(models.Model):
    pass_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE , related_name='%(class)s_requests_created', null=True)
    college = models.ForeignKey(College,on_delete=models.CASCADE , related_name='%(class)s_requests_created', null=True)
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE , related_name='%(class)s_requests_created', null=True)
    valid_from = models.DateField(null=True)
    valid_to = models.DateField(null=True)
    payment = models.BooleanField(default=False)
    pass_file = models.ImageField(upload_to='home/pass', default="" )

class AuthUser(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,default="",null=True)
    type = models.SmallIntegerField(null=True)
    student_id = models.ForeignKey(Student,related_name='%(class)s_student',on_delete=models.CASCADE ,null=True )
    college_id = models.ForeignKey(College,related_name='%(class)s_college',on_delete=models.CASCADE ,null=True )
    manager_id = models.ForeignKey(Manager,related_name='%(class)s_manager',on_delete=models.CASCADE ,null=True )

""" @receiver(post_save, sender=User)
def create_user_AuthUser(sender, instance, created, **kwargs):
    if created:
        AuthUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_AuthUser(sender, instance, **kwargs):
    instance.authuser.save()
"""