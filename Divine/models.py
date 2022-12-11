from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.utils import timezone
from birthday import BirthdayField, BirthdayManager
import datetime
from django.urls import reverse
# Create your models here.


GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

POSITION = [
    ('Member', 'Member'),
    ('President', 'President'),
    ('Brothers Co-ordinator', 'Brothers Co-ordinator'),
    ('Senior Colleague', 'Senior Colleague'),
]

UNIT = [
    ('Ushery', 'Ushery'),
    ('Music', 'Music'),
    ('Library', 'Library'),
    ('Drama', 'Drama'),
    ('Media', 'Media'),
]


LEVEL_OF_STUDY = [
    ('100 level', '100 level'),
    ('200 level', '200 level'),
    ('300 level', '300 level'),
    ('400 level', '400 level'),
    ('500 level', '500 level'),
    ('Final year', 'Final year'),
    ('Not a student', 'Not a student')
]


class CustomUser(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(unique = True)
    
    dept = models.CharField(max_length=50, blank=True)
    faculty = models.CharField(max_length=50, blank=True)
    student = models.BooleanField(default=False)
    unit = models.CharField(max_length=50, choices=UNIT, blank=True)
    gender = models.CharField(max_length=8, choices=GENDER)
    phone_number = models.CharField(max_length=15)
    skill_or_talent = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=22, choices=POSITION, default='Member')
    address = models.CharField(max_length=120,  blank=True)
    town = models.CharField(max_length=50,  blank=True)
    state = models.CharField(max_length=50,  blank=True)
    level = models.CharField(max_length=13, choices=LEVEL_OF_STUDY, default='Not a student')
    twitter = models.CharField(max_length=120, blank=True)
    facebook = models.CharField(max_length=120, blank=True)
    instagram = models.CharField(max_length=120, blank=True)
    whatsapp = models.CharField(max_length=120, blank=True)
    image = models.ImageField(upload_to='profileImages', default='default.jpg')
    exco = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return "{}".format(self.email)
    
    def get_absolute_url(self):
        return reverse('members_detail', kwargs={'pk' : self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if (img.height < 340 or img.height > 340) or (img.width < 360 or img.width > 360):
            output_size = (360, 340)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
    
    
class UserBirthday(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    birthday = BirthdayField(default=datetime.date.today)  # birthday field from django-birthday
    
    objects = BirthdayManager() #birthdayManager from django-birthday




class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='activityImages')
    date_created = models.DateTimeField(default=timezone.now)
    date_of_event = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.title[:20]

    def get_absolute_url(self):
        return reverse('activity_detail', kwargs={'pk' : self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if (img.height < 400 or img.height > 400) or (img.width < 750 or img.width > 750):
            output_size = (750, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
            


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    comment = models.TextField()
    date_commented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.comment} by {self.member.username}'
    
    
    
class Ebook(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=150)
    image = models.ImageField(upload_to='ebookImages')
    file = models.FileField(upload_to='ebookFiles')
    date_uploaded = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'Book: {self.name} by {self.author}'

    # def get_absolute_url(self):
    #     return reverse('ebook_detail', kwargs={'pk' : self.pk})


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if (img.height < 280 or img.height > 280) or (img.width < 555 or img.width > 555):
            output_size = (555, 280)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
            



class HomeData(models.Model):
    background_image = models.ImageField(upload_to='home')
    whatsapp = models.CharField(max_length=20)
    grid1 =  models.ImageField(upload_to='home')
    grid2 =  models.ImageField(upload_to='home')
    grid3 =  models.ImageField(upload_to='home')
    grid4 =  models.ImageField(upload_to='home')
    grid5 =  models.ImageField(upload_to='home')
    grid6 =  models.ImageField(upload_to='home')
    motto = models.CharField(max_length=100)
    about = models.TextField()
    
    class Meta:
        verbose_name_plural = 'HomeData'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.background_image.path)
        if (img.height < 400 or img.height > 400) or (img.width < 750 or img.width > 750):
            output_size = (750, 400)
            img.thumbnail(output_size)
            img.save(self.background_image.path)
            
            
            


class GrowthMaterial(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Material: {self.title}'
    
    
    


class Gallery(models.Model):
    image = models.ImageField(upload_to='galleryImages')
    description = models.TextField()
    class Meta:
        verbose_name_plural = 'Gallery'






class AnonymousMessage(models.Model):
    name = models.CharField(max_length=30, default="Anonymous")
    email = models.EmailField(default="anonymous@gmail.com")
    title = models.CharField(max_length=30)
    message = models.TextField()
    
    def __str__(self):
        return f'{self.name} : {self.title}'