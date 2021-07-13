from django.db import models

# Create your models here.


class BeforeAndAfter(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'photos/before_and_after/%y/%m/%d')
    feature = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'BeforeAndAfter'
        verbose_name_plural = 'BeforeAndAfter'

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    photo = models.ImageField(upload_to = 'photos/about_us/%y/%m/%d')
    description = models.TextField()

    class Meta:
        verbose_name = 'AboutUs'
        verbose_name_plural = 'AboutUs'

class Home(models.Model):
    logo = models.ImageField(upload_to = 'photos/logo/%y/%m/%d')
    FAQ = models.CharField(max_length=250)
    blog = models.CharField(max_length=250)
    intro_image = models.ImageField(upload_to = 'photos/home/%y/%m/%d')
    intro_text = models.TextField()
    about_us_image = models.ImageField(upload_to = 'photos/home/%y/%m/%d')
    about_us_text = models.TextField()

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'


class Footer(models.Model):
    facebook = models.CharField(max_length=100, default="https://www.facebook.com/", null=True, blank=True)
    instagram = models.CharField(max_length=100, default="https://www.instagram.com", null=True, blank=True)
    youtube = models.CharField(max_length=100, default="https://www.instagram.com", null=True, blank=True)
    twitter = models.CharField(max_length=100, default="https://twitter.com/", null=True, blank=True)
    address = models.CharField(max_length=100, default="", null=True, blank=True)
    email =  models.CharField(max_length=100, null=True, blank=True)
    first_phone_number =  models.CharField(max_length=100, null=True, blank=True)
    second_phone_number =  models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'

class FAQ(models.Model):
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)