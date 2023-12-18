from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        ordering = ['-created_at']
        
class Student(BaseModel):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    adhar_card_number = models.CharField(max_length=16)
    dob = models.DateField()
    identification_marks = models.TextField()
    admission_category = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    mail_id = models.EmailField(unique=True)
    contact_detail = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self) -> str:
        return self.id
    
class Parent(BaseModel):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=255)
    father_qualification = models.CharField(max_length=50)
    father_profession = models.CharField(max_length=50)
    father_designation = models.CharField(max_length=50)
    father_aadhar_card = models.CharField(max_length=16)
    father_mobile_number = models.CharField(max_length=20)
    father_mail_id = models.EmailField(unique=True)
    mother_name = models.CharField(max_length=255)
    mother_qualification = models.CharField(max_length=50)
    mother_profession = models.CharField(max_length=50)
    mother_designation = models.CharField(max_length=50)
    mother_aadhar_card = models.CharField(max_length=16)
    mother_mobile_number = models.CharField(max_length=20)
    mother_mail_id = models.EmailField()

class AcademicDetails(BaseModel):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    enrollment_id = models.CharField(max_length=50)
    class_name = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    doj = models.DateField()

class Document(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to="document/", null=True, blank=True)

