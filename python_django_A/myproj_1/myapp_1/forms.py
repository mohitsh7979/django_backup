from django import forms 


# class student_forms(forms.ModelForm):

#     class Meta:

#         model = student
#         fields = ('__all__')




# class myform(forms.Form):

#     name = forms.CharField()
#     email = forms.EmailField()
#     address = forms.CharField()

class profile_form(forms.Form):
    name = forms.CharField()
    father_name = forms.CharField()
    mother_name = forms.CharField()
    email = forms.EmailField()
    roll_no = forms.IntegerField()
    stream = forms.CharField()
    address = forms.CharField()
    state = forms.CharField()
    city = forms.CharField()
    pin_code = forms.CharField()
    gender = forms.CharField()
    mobile_no = forms.CharField()
    image = forms.ImageField()
    descripation = forms.CharField()
    



