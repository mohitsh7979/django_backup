from django.db import models

# class Education(models.Model):
#     school = models.CharField(max_length=100)
#     degree = models.CharField(max_length=100)
#     year = models.CharField(max_length=4)

# class Skill(models.Model):
#     name = models.CharField(max_length=100)

# class Language(models.Model):
#     name = models.CharField(max_length=100)

# class Interest(models.Model):
#     name = models.CharField(max_length=100)

# class Resume(models.Model):
#     full_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)
#     github = models.URLField()
#     linkdin = models.URLField()
#     address = models.TextField()
#     educations = models.ManyToManyField(Education)
#     skills = models.ManyToManyField(Skill)
#     languages = models.ManyToManyField(Language)
#     interests = models.ManyToManyField(Interest)

#     def __str__(self):
#         return self.full_name



# class resume_model(models.Model):
#         full_name = models.CharField(max_length=100)
#         email = models.CharField(max_length=100)
#         phone_number = models.CharField(max_length=100)
#         github = models.CharField(max_length=100)
#         linkdin = models.CharField(max_length=100)
#         address = models.CharField(max_length=100)
#         school = models.CharField(max_length=100)
#         degree = models.CharField(max_length=100)
#         year = models.CharField(max_length=100)
#         school_1 = models.CharField(max_length=100)
#         degree_1 = models.CharField(max_length=100)
#         year_1 = models.CharField(max_length=100)
#         school_2 = models.CharField(max_length=100)
#         degree_2 = models.CharField(max_length=100)
#         year_2 = models.CharField(max_length=100)
#         skill = models.CharField(max_length=100)
#         skill_1 = models.CharField(max_length=100)
#         skill_2 = models.CharField(max_length=100)
#         skill_3 = models.CharField(max_length=100)
#         skill_4 = models.CharField(max_length=100)
#         skill_5 = models.CharField(max_length=100)
#         skill_6 = models.CharField(max_length=100)
#         skill_7 = models.CharField(max_length=100)
#         skill_8 = models.CharField(max_length=100)
#         skill_9 = models.CharField(max_length=100)
#         language = models.CharField(max_length=100)
#         language_1 = models.CharField(max_length=100)
#         language_2 = models.CharField(max_length=100)
#         interest = models.CharField(max_length=100)
#         interest_1 = models.CharField(max_length=100)
#         interest_2 = models.CharField(max_length=100)


from django.db import models

class Resume(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    year = models.CharField(max_length=4)

class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
