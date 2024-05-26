from django.forms import ModelForm
from searchApp.models import JobPosting, JobDescription, JobCategory

from django import forms
from .models import JobPosting, JobDescription

class JobPostingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['job_category'] = forms.ModelChoiceField(queryset=JobCategory.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
        
    class Meta:
        model = JobPosting
        # exclude = ['posted_by', 'date_posted', ]
        fields = ['job_title', 'company_name', 'location', 'job_category', 'employment_type', 'salary_range', 'closing_date', 'logo', 'company_info', 'company_web', 'company_email']

        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
            # 'job_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Job Description'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of your company'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location of your company'}),
            'salary_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Salary range per year'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
            'company_info': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Company Information'}),
            'company_web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Company web address'}),
            'company_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Company email address'}),
            'employment_type': forms.Select(attrs={'class': 'form-control'}),
            'closing_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'job_title': 'Job Title',
            # 'job_description': 'Job Description',
            'company_name': 'Company Name',
            'location': 'Location',
            'salary_range': 'Salary Range',
            'logo': 'Company Logo',
            'company_info': 'Company Information',
            'company_web': 'Company Website',
            'company_email': 'Company Email',
            'employment_type': 'Employment Type',
            'closing_date': 'Closing Date',
            'job_category': 'Job Category',
        }
class JobDescriptionForm(forms.ModelForm):
    class Meta:
        model = JobDescription
        # exclude = ['job', ]
        fields = ['description', 'required_knowledge', 'education_experience']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Job Description'}),
            'requirement': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Required Knowledge, Skills, and Abilities'}),
            'education': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Education + Experience'}),
        }