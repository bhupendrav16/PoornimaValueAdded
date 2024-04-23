from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from courses.models import Branch, Semester,Course, Subject

class CustomUserManager(BaseUserManager):

    def create_user(self, email, name, registration_no, contact_info, password=None,profile_picture=None, is_faculty=False, **extra_fields):
        if not name:
            raise ValueError("Username must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, registration_no=registration_no,contact_info=contact_info, 
                          profile_picture=profile_picture,
                          is_faculty=is_faculty, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email,  name, contact_info, registration_no,password=None, profile_picture=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, name, contact_info,registration_no, password, profile_picture=profile_picture,is_faculty=True, **extra_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    registration_no = models.CharField(max_length =100,unique=True)
    contact_info = PhoneNumberField(null=False, blank=False, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)  
    
    # for student
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True, blank=True)

    #for faculty
    subjects = models.ManyToManyField(Subject, blank=True)
    
    is_faculty = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    def str(self):
        return self.name
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['registration_no','contact_info','name']

    