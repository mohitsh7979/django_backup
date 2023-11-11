from django.shortcuts import render
# from .models import resume_model

# # # Create your views here.


def resume_output(request):
    return render(request,'resume.html')

# def resume_form(request):

#     if request.method == "POST":
        
#         full_name = request.POST['full_name']
#         email = request.POST['email']
#         phone_number = request.POST['phone']
#         github = request.POST['github']
#         linkdin = request.POST['linkdin']
#         address = request.POST['address']
#         school = request.POST['education_school']
#         degree = request.POST['education_degree']
#         year = request.POST['education_year']
#         school_1 = request.POST['education_1_school']
#         degree_1 = request.POST['education_1_degree']
#         year_1 = request.POST['education_1_year']
#         school_2 = request.POST['education_2_school']
#         degree_2 = request.POST['education_2_degree']
#         year_2 = request.POST['education_2_year']
#         skill = request.POST['skill_name']
#         skill_1 = request.POST['skill_name']
#         skill_2 = request.POST['skill_1_name']
#         skill_3 = request.POST['skill_2_name']
#         skill_4 = request.POST['skill_3_name']
#         skill_5 = request.POST['skill_4_name']
#         skill_6 = request.POST['skill_5_name']
#         skill_7 = request.POST['skill_6_name']
#         skill_8 = request.POST['skill_7_name']
#         skill_9 = request.POST['skill_8_name']
#         language = request.POST['language']
#         language_1 = request.POST['language_1']
#         language_2 = request.POST['language_2']
#         interest = request.POST['interest']
#         interest_1 = request.POST['interest_1']
#         interest_2 = request.POST['interest_2']


#         resume_model(full_name=full_name,email=email,phone_number=phone_number,github=github,linkdin=linkdin,address=address,school=school,degree=degree,year=year,school_1=school_1,degree_1=degree_1,year_1=year_1,school_2=school_2,degree_2=degree_2,year_2=year_2,skill=skill,skill_1=skill_1,skill_2=skill_2,skill_3=skill_3,skill_4=skill_4,skill_5=skill_5,skill_6=skill_6,skill_7=skill_7,skill_8=skill_8,skill_9=skill_9,language=language,language_1=language_1,language_2=language_2,interest=interest,interest_1=interest_1,interest_2=interest_2).save()

#         print(full_name,email,phone_number,github,linkdin,address,school,school_1,skill_1,skill_3)
      
   

       


# from django.shortcuts import render, redirect
# from .models import Resume, Education, Skill, Language, Interest

# def resume_form(request):
#     if request.method == 'POST':
#         full_name = request.POST['full_name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         github = request.POST['github']
#         linkdin = request.POST['linkdin']
#         address = request.POST['address']

#         # Create a new Resume object
#         new_resume = Resume(
#             full_name=full_name,
#             email=email,
#             phone=phone,
#             github=github,
#             linkdin=linkdin,
#             address=address,
#         )
#         new_resume.save()

#         # Process and save education data
#         education_fields = request.POST.getlist('education_school')
#         print(education_fields,'>>>>>>>>>>education_fields')
#         for i in range(0,2):
#             school = request.POST.getlist(f'education_{[i]}_school')
#             degree = request.POST.getlist(f'education_{[i]}_degree')
#             year = request.POST.getlist(f'education_{[i]}_year')
#             education = Education(school=school, degree=degree, year=year)
#             print(school,degree,year)
#             education.save()
#             new_resume.educations.add(education)

#         # Process and save skill data
#         skill_fields = request.POST.getlist('skill_name')
#         print(skill_fields,'>>>>>>>>>>skill_fields')
#         for skill_name in skill_fields:
#             skill = Skill(name=skill_name)
#             skill.save()
#             new_resume.skills.add(skill)

#         # Process and save language data
#         language_fields = request.POST.getlist('language_name')
#         print(language_fields,'>>>>>>>>>language_fields')
#         for language_name in language_fields:
#             language = Language(name=language_name)
#             language.save()
#             new_resume.languages.add(language)

#         # Process and save interest data
#         interest_fields = request.POST.getlist('interest_name')
#         for interest_name in interest_fields:
#             interest = Interest(name=interest_name)
#             interest.save()
#             new_resume.interests.add(interest)

#         return redirect('success_page')  # Redirect to a success page

#     return render(request, 'resume_form.html')




from .models import Resume, Education, Skill

def resume_form(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']

        # Create a new Resume object
        new_resume = Resume(
            full_name=full_name,
            email=email,
            phone=phone,
            address=address,
        )
        new_resume.save()

        # Process and save education data
        education_fields = request.POST.getlist('education_school')
        print(education_fields,'>>>>>>education fields')
        degree_fields = request.POST.getlist('education_degree')
        year_fields = request.POST.getlist('education_year')
        for i in range(len(education_fields)):
            school = education_fields[i]
            degree = degree_fields[i]
            year = year_fields[i]
            education = Education(resume=new_resume, school=school, degree=degree, year=year)
            education.save()

        # Process and save skill data
        skill_fields = request.POST.getlist('skill_name')
        for skill_name in skill_fields:
            skill = Skill(resume=new_resume, name=skill_name)
            skill.save()

        return redirect('success_page')  # Redirect to a success page

    return render(request, 'resume_form.html')
