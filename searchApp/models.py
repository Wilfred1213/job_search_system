from django.db import models
from authentication.models import CustomUser
from django.utils import timezone


class JobCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

# class EmploymentType(models.Model):
#     name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class JobPosting(models.Model):
    EMPLOYMENT_TYPES = [
    ('Full time', 'Full time'),
    ('Part time', 'Part time'),
    ('Internship', 'Internship'),
    
]
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    job_title = models.CharField(max_length=255)
    # job_description = models.TextField()
    company_name = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255)
    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    employment_type = models.CharField(max_length=255, choices=EMPLOYMENT_TYPES, null=True)# Full-time, Part-time, Internship, etc.
    salary_range = models.CharField(max_length=255)  # Optional
    date_posted = models.DateTimeField(auto_now_add=True)
    closing_date = models.DateField(default=timezone.now)
    logo = models.ImageField(upload_to='company_logo/', null = True)
    company_info =models.TextField(max_length=1000, null=True)
    # company_name = models.CharField(max_length=255, null=True)
    company_web = models.URLField(max_length=255, null=True)
    company_email = models.EmailField(max_length=255, null=True)



    def __str__(self):
        return self.job_title
    
class JobDescription(models.Model):
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    description = models.TextField()
    required_knowledge = models.TextField(max_length=2000)
    education_experience = models.TextField(max_length=2000)
    

class JobApplication(models.Model):
    STATUS = [
        ('PENDING', 'Pending'),
        ('REJECTED', 'Rejected'),
        ('INTERVIEW', 'Interview'),
        ('EMPLOYED', 'Employed'),
    ]
    
    full_name =models.CharField(max_length=255, null=True)
    state =models.CharField(max_length=255, null=True)
    lga =models.CharField(max_length=255, null=True)
    expected_salary = models.CharField(max_length=255, null=True)
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    cover_letter = models.FileField(upload_to='cover_letters', null=True, blank=True)  # Optional
    year_of_experience =models.IntegerField(default=0)
    date_of_birth = models.DateField(default=timezone.now)
    resume_file = models.FileField(upload_to='resumes/', null=True)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=STATUS, null=True)  # Pending, Rejected, Interview Scheduled, etc.