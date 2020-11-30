from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Course(models.Model):
    CourseCode = models.CharField(max_length=60)
    subjectTitle = models.CharField(max_length=255)
    creditUnits = models.IntegerField()
    score = models.IntegerField()
    grade = models.CharField(max_length=1)
    point = models.FloatField()
     

    def __str__(self):
        return f'{self.CourseCode} - {self.subjectTitle} - {self.creditUnits}'



class MyAccountManager(BaseUserManager):
    def create_user(self, email, matric_number, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not matric_number:
            raise ValueError("User must have a matric number")
        user = self.model(
            email=self.normalize_email(email),
            matric_number=matric_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    STUDY_LEVEL_CHOICES = [
        (100, 'ND 1'),
        (200, 'ND 2'),
    ]
    ACADEMIC_SESSION_CHOICES = [
        ('first semester', 'First Semester'),
        ('second semester', 'Second Semester'),
    ]

    DEPARTMENT_CHOICES = [
        ('Accountancy', 'Accountancy'),
        ('Business Admin', 'Business Admin'),
        ('Computer Science', 'Computer Science'),
        ('Statistics', 'Statistics'),
    ]

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    matric_number = models.CharField(max_length=60, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    department = models.CharField(max_length=60, choices=DEPARTMENT_CHOICES, default='Accountancy')
    study_level = models.IntegerField(choices=STUDY_LEVEL_CHOICES, default=100)
    academic_session = models.CharField(
        choices=ACADEMIC_SESSION_CHOICES, max_length=30, default='first semester')
    courses = models.ManyToManyField(Course)

    USERNAME_FIELD = 'matric_number'  # specify which field u want the user to use to login
    REQUIRED_FIELDS = ['email']
    

    objects = MyAccountManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name} Matric Number: {self.matric_number}'

    # The following methods are compulsory

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True




class Complain(models.Model):
    description = models.TextField(blank=True)

    def __str__(self):
        return self.description[:15]



