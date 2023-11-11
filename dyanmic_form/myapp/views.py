from django.shortcuts import render, redirect
from .models import PersonalInformation, Education, Skill
from .forms import PersonalInformationForm, EducationForm, SkillForm

def resume_form(request):
    if request.method == 'POST':

        full_name = request.POST['personal_info-full_name']
        email = request.POST['personal_info-email']
        phone = request.POST['personal_info-phone']
        address = request.POST['personal_info-address']
        school = request.POST['education-school']
        degree = request.POST['education-degree']
        year = request.POST['education-year']
        school1 = request.POST['education-1-school']
        degree1 = request.POST['education-1-degree']
        year1 = request.POST['education-1-year']
        school2 = request.POST['education-2-school']
        degree2 = request.POST['education-2-degree']
        year2 = request.POST['education-2-year']
        skill1 = request.POST['skill-name']
        skill2 = request.POST['skill-1-name']
        skill3 = request.POST['skill-2-name']

        print(full_name,email,phone,address,school,degree,year,school1,degree1,year1,school2,degree2,year2,skill1,skill2,skill3)


       
        # personal_info_form = PersonalInformationForm(request.POST, prefix='personal_info')
        # education_form = EducationForm(request.POST, prefix='education')
        # print('>>',education_form)
        # skill_form = SkillForm(request.POST, prefix='skill')

        # if personal_info_form.is_valid() and education_form.is_valid() and skill_form.is_valid():
        #     personal_info = personal_info_form.save()

        #     for i in education_form:
        #         name = i.cleaned_data['education_school']
        #         print(name)


            # education_instances = []
            # for education_formset in education_form:
            #     education_formset.save()
                # print('>>>>>>>>>>>',education_formset)
                # if education_formset.is_valid():
                #     education = education_formset.save(commit=False)
                #     education.personal_info = personal_info
                #     education.save()
                #     education_instances.append(education)

            # skill_instances = []
            # for skill_formset in skill_form:
            #     if skill_formset.is_valid():
            #         skill = skill_formset.save(commit=False)
            #         skill.personal_info = personal_info
            #         skill.save()
            #         skill_instances.append(skill)

            # return redirect('success')  # Redirect to a success page after form submission
        # else:
        #     print('Error:', personal_info_form.errors, education_form.errors, skill_form.errors)
    else:
        personal_info_form = PersonalInformationForm(prefix='personal_info')
        education_form = EducationForm(prefix='education')
        skill_form = SkillForm(prefix='skill')

    return render(request, 'resume_form.html', {
        'personal_info_form': personal_info_form,
        'education_form': education_form,
        'skill_form': skill_form,
    })

def success(request):
    return render(request, 'success.html')
