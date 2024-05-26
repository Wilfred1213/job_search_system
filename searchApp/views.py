from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from searchApp.models import JobApplication, JobDescription, JobCategory, JobPosting
from django.contrib import messages
from django.db.models import Count, Q
from searchApp.forms import JobDescriptionForm, JobPostingForm
from django.core.paginator import Paginator




# Create your views here.
def index(request):
    if request.method =='GET':
        search = request.GET.get('search')

        jobs = JobDescription.objects.filter(Q(job__job_title__icontains = search)|Q(job__location__icontains = search)) if search else None
        location = JobCategory.objects.annotate(get_count = Count('jobposting__job_title'))
        recent_jobs = JobDescription.objects.all().order_by('-job__date_posted')[:4]
    
        
    context = {
        'jobs':jobs,
        'locations':location,
        'recents':recent_jobs

    
    }
    return render(request, 'searchApp/index.html', context)


def job_category(request, cat_id):
    try:
        category = JobCategory.objects.get(id=cat_id)
    except JobCategory.DoesNotExist:
        category = None
    

    get_category = category.jobposting_set.all()
    counting = get_category.count()

    context = {
        'jobs': get_category,
        'count': counting,
        'category_id': cat_id  # Pass the category ID to the context
    }
    return render(request, 'searchApp/category.html', context)

def job_category_detail(request, cat_id):
    try:
        job = JobPosting.objects.get(id=cat_id)
        job_description = JobDescription.objects.get(job=job)
    except (JobPosting.DoesNotExist, JobDescription.DoesNotExist):
        job = None
        job_description = None

    context = {
        'job': job,
        'job_description': job_description
    }
    return render(request, 'searchApp/job_category_details.html', context)
def add_job(request):
    user = request.user
    all_category = JobCategory.objects.all()

    if request.method == 'POST':
        forms = JobPostingForm(request.POST, request.FILES)
        forms_desc = JobDescriptionForm(request.POST)

        if forms.is_valid() and forms_desc.is_valid():
            print("Forms are valid")
            save_posting = forms.save(commit=False)
            save_posting.posted_by = user
            save_posting.save()
            print("Job posting saved")
            
            save_desc = forms_desc.save(commit=False)
            save_desc.job = save_posting  # Link the JobDescription to JobPosting
            save_desc.save()
            print("Job description saved")

            messages.info(request, 'Job posted successfully')
            return redirect('add_job')
    else:
        forms = JobPostingForm()
        forms_desc = JobDescriptionForm()

    context = {
        'categories': all_category,
        'form': forms,
        'form_desc': forms_desc
    }
    return render(request, 'searchApp/add_job.html', context)
 

def job_listing(request):
    jobs = JobDescription.objects.all()
    paginator = Paginator(jobs, 10)  # Show 10 jobs per page
    page_number = request.GET.get('page')
    jobs_paginated = paginator.get_page(page_number)
    count = jobs.aggregate(counting=Count('job'))
    context = {
        'jobs': jobs_paginated,
        'count': count,
    }
    return render(request, 'searchApp/job_listing.html', context)

def job_details(request, job_id):
    try:
        job = JobDescription.objects.get(id=job_id)
    except JobDescription.DoesNotExist:
        job = None


    context = {
        'job': job,
        
    }
    return render(request, 'searchApp/job_details.html', context)


# def job_details(request, job_id, cat_id):
#     job = JobDescription.objects.get(id=job_id)
#     cat_id = JobCategory.objects.get(id=cat_id)
#     category_id = JobDescription.objects.get(id=cat_id)
    

#     context = {
#         'job':job,
#         'category_id':category_id
        
        
#     }
#     return render(request, 'searchApp/job_details.html', context)

def application(request, job_id):
    user = request.user
    job = JobPosting.objects.get(id=job_id)
    if request.method =='POST':
        name = request.POST.get('name')
        state= request.POST.get('state')
        lga= request.POST.get('lga')
        experience= request.POST.get('experience')
        dob= request.POST.get('dob')
        resume= request.POST.get('resume')
        salary= request.POST.get('salary')
        letter= request.POST.get('letter')

        save_application = JobApplication(applicant = user, job_posting=job,
                                          full_name = name, state = state,
                                          lga = lga, year_of_experience=experience,
                                          date_of_birth= dob, resume_file= resume,
                                          expected_salary= salary, status = 'PENDING',
                                          cover_letter = letter)
        save_application.save()
        messages.info(request, f'You applied for the position of {job.job_title}')
        return redirect('application', job_id)

    context = {
        'job':job,
        
    }
    return render(request, 'searchApp/application.html', context)



