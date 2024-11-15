from django.db import models

# Create your models here.
class About(models.Model):
    image = models.ImageField(upload_to='static/images')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    resume = models.CharField(max_length=100)
    experience = models.IntegerField()
    project_sucess = models.IntegerField()
    rate = models.IntegerField()
    logo = models.ImageField(upload_to='static/images')
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    freelace_status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Education(models.Model):
    academy_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField( null=True, blank=True)
    description = models.TextField()
    
    def __str__(self):
        return self.academy_name

class Skill(models.Model):
    value = models.IntegerField()
    bg = models.CharField(max_length=100)
    skill_name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.skill_name
class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField( null=True, blank=True)
    description = models.TextField()
    
    def __str__(self):
        return self.company_name

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images')
    description = models.TextField()
    source_code = models.URLField(max_length=200)
    view_project = models.URLField(max_length=200)
    video = models.URLField(max_length=200)
    
    def __str__(self):
        return self.project_name

class Service(models.Model):
    service_name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.service_name

class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.contact_name

class Link(models.Model):
    link_name = models.CharField(max_length=100)
    link_url = models.URLField(max_length=200)
    icon = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.link_name

class Certificate(models.Model):
    certificate_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/images/certificate')
    category = models.ForeignKey('Category_Certificate', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.certificate_name

class Category_Certificate(models.Model):
    category_name = models.CharField(max_length=100)    
    def __str__(self):
        return self.category_name