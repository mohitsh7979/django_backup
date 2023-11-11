# from django import forms
# from django.forms import formset_factory
# from .models import Education, Skill, PersonalInfo

# class EducationForm(forms.ModelForm):
#     class Meta:
#         model = Education
#         fields = ['school', 'degree', 'year']

# class SkillForm(forms.ModelForm):
#     class Meta:
#         model = Skill
#         fields = ['name']

# class PersonalInfoForm(forms.ModelForm):
#     class Meta:
#         model = PersonalInfo
#         fields = ['full_name', 'email', 'phone', 'address']

# # Create formsets for Education and Skill
# EducationFormset = formset_factory(EducationForm, extra=1, can_delete=True)
# # SkillFormset = formset_factory(SkillForm, extra=1, can_delete=True)

# class ResumeForm(forms.Form):

#     educations = EducationFormset()


from django import forms
from .models import PersonalInformation, Education, Skill

class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = '__all__'

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

   
