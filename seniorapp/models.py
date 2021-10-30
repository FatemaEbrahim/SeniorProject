from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class StudentManager(BaseUserManager):
    def create_user(self, id, name,cpr, gpa, college, department, course, password):
        """
        Creates and saves a Student with the given student ID, date of
        birth and password.
        """
        if not id:
            raise ValueError('Student must fill a student id')
        if not name:
            raise ValueError('Student must fill a student name')
        if not cpr:
            raise ValueError('Student must fill a student cpr')
        if not gpa:
            raise ValueError('Student must fill a student gpa')
        if not college:
            raise ValueError('Student must fill a student college')
        if not department:
            raise ValueError('Student must fill an student department')
        if not course:
            raise ValueError('Student must fill an student course') 
        if not password:
            raise ValueError('Student must fill a password')    

        student = self.model(
            id=id,
            name=name,
            cpr=cpr,
            gpa=gpa,
            college=college,
            department=department,
            course=course,
        )

        student.set_password(password)
        student.save(using=self._db)
        return student



# Create your models here.
class Student(AbstractBaseUser):
    type = models.CharField(max_length=7, default='student', editable=False)
    academic_id = models.CharField(max_length=8, unique=True)
    password = models.CharField(max_length=32)
    cpr = models.CharField(max_length=9, unique=True)
    name = models.CharField(max_length=50)
    gpa = models.FloatField(default=3.0)
    college = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    course = models.CharField(max_length=7)
    number = models.CharField(max_length=8, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    nationality = models.CharField(max_length=32)
    photo = models.FileField(upload_to='student_photo/')
    resume = models.FileField(upload_to='resume_pdf/')
    transcript = models.FileField(upload_to='transcript_pdf/')

    objects = StudentManager()

    USERNAME_FIELD = 'academic_id'
    REQUIRED_FIELDS = ['cpr', 'name', 'gpa', 'college', 'department', 'course']

    def __str__(self):
        return self.name
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    class Meta:
        permissions = [
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        ]

class Recommendation(models.Model):
    doctor = models.CharField(max_length=50)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='recommendation_pdf/')
    upload_date = models.DateTimeField('Recommendation Upload Date', auto_now_add=True, blank=True)

class Company(models.Model):
    type = models.CharField(max_length=7, default='company', editable=False)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500)
    photo = models.FileField(upload_to='company_photo/')
    number = models.CharField(max_length=8, unique=True)

class Coordinator(models.Model):
    type = models.CharField(max_length=11, default='coordinator', editable=False)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=200)
    photo = models.FileField(upload_to='coordinator_photo/')
    number = models.CharField(max_length=8, unique=True)

class College(models.Model):
    college = models.CharField(max_length=50, unique=True)

class Opportunity(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    college = models.ForeignKey(Student, on_delete=models.CASCADE)
    oppotunity_title = models.CharField(max_length=50)
    oppotunity_description = models.TextField(max_length=500)
    add_date = models.DateTimeField('Opportunity Add Date', auto_now_add=True, blank=True)

    

class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    application_date = models.DateTimeField('Application Date', auto_now_add=True, blank=True)

class Acceptance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='acceptance_pdf/')
    upload_date = models.DateTimeField('Acceptance Upload Date', auto_now_add=True, blank=True)

class FinalReport(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    final_report_pdf = models.FileField(upload_to='student_photo/')
    final_report_submission_date = models.DateTimeField('date submitted')
    final_report_question_01 = models.CharField(max_length=32)
    final_report_question_02 = models.CharField(max_length=32)
    final_report_question_03 = models.CharField(max_length=32)
    final_report_question_04 = models.CharField(max_length=32)
    final_report_question_05 = models.CharField(max_length=32)
    final_report_question_06 = models.CharField(max_length=32)
    final_report_question_07 = models.CharField(max_length=32)
    final_report_question_08 = models.CharField(max_length=32)

class CompanyEvaluation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_evaluation_pdf = models.FileField(upload_to='student_photo/')
    company_evaluation_submission_date = models.DateTimeField('date submitted')
    company_evaluation_question_01 = models.CharField(max_length=32)
    company_evaluation_question_02 = models.CharField(max_length=32)
    company_evaluation_question_03 = models.CharField(max_length=32)
    company_evaluation_question_04 = models.CharField(max_length=32)
    company_evaluation_question_05 = models.CharField(max_length=32)
    company_evaluation_question_06 = models.CharField(max_length=32)
    company_evaluation_question_07 = models.CharField(max_length=32)
    company_evaluation_question_08 = models.CharField(max_length=32)

class CoordinatorEvaluation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    coordinator = models.ForeignKey(Coordinator, on_delete=models.CASCADE)
    coordinator_evaluation_pdf = models.FileField(upload_to='student_photo/')
    coordinator_evaluation_submission_date = models.DateTimeField('date submitted')
    coordinator_evaluation_question_01 = models.CharField(max_length=32)
    coordinator_evaluation_question_02 = models.CharField(max_length=32)
    coordinator_evaluation_question_03 = models.CharField(max_length=32)
    coordinator_evaluation_question_04 = models.CharField(max_length=32)
    coordinator_evaluation_question_05 = models.CharField(max_length=32)
    coordinator_evaluation_question_06 = models.CharField(max_length=32)
    coordinator_evaluation_question_07 = models.CharField(max_length=32)
    coordinator_evaluation_question_08 = models.CharField(max_length=32)
