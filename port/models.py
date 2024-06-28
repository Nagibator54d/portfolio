from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    contact_email = models.EmailField()
   

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Профиль'
        verbose_name_plural='Профиль'

class Skill(models.Model):
    profile = models.ForeignKey(Profile, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField(help_text="Proficiency level from 1 to 10")

    def __str__(self):
        return f"{self.name} ({self.proficiency})"

    class Meta:
        verbose_name='Навыки'
        verbose_name_plural='Навыки'

class Project(models.Model):
    profile = models.ForeignKey(Profile, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='proj ect_images/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Проекты'
        verbose_name_plural='Проекты'

class Experience(models.Model):
    profile = models.ForeignKey(Profile, related_name='experiences', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"

    class Meta:
        verbose_name='Опыт работы'
        verbose_name_plural='Опыт работы'

class Education(models.Model):
    profile = models.ForeignKey(Profile, related_name='educations', on_delete=models.CASCADE)
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.degree} at {self.school}"

    class Meta:
        verbose_name='Обучение'
        verbose_name_plural='Обучение'
