# from django.db import models

# class Education(models.Model):
#     school = models.CharField(max_length=100)
#     degree = models.CharField(max_length=100)
#     year = models.CharField(max_length=4)

#     def __str__(self):
#         return f"{self.degree} from {self.school}, {self.year}"

# class Skill(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class PersonalInfo(models.Model):
#     full_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)
#     address = models.TextField()

#     def __str__(self):
#         return self.full_name



from django.db import models

class PersonalInformation(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.full_name

class Education(models.Model):
    # personal_info = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.school

class Skill(models.Model):
    # personal_info = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


